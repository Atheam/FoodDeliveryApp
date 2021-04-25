from django.shortcuts import render
from django.http import HttpResponse
from Users.models import Restaurants    
from OrderManagement.models import Menu,MenuDetails,Dish  
from OrderManagement.forms import add_dish_form
from django.shortcuts import redirect

def manage_menu(request):
    restaurant = Restaurants.objects.filter(user = request.user)[0]
    menu = Menu.objects.filter(restaurant = restaurant)[0]
    details = MenuDetails.objects.filter(menu = menu)

    args = {'details':details}
    return render(request,'OrderManagement/menuManagement.html',args)

def add_dish(request):
    if request.method == "POST":
        form = add_dish_form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            description = form.cleaned_data['description']
            dish = Dish(name = name,price= price,description=description)
            dish.save()
            restaurant = Restaurants.objects.filter(user = request.user)[0]
            menu = Menu.objects.filter(restaurant = restaurant)[0]
            menu_details = MenuDetails(dish = dish,menu = menu)
            menu_details.save()
            return redirect('manageMenu')
    else:
        form = add_dish_form()
    
    return render(request,'OrderManagement/addDish.html',{'form':form})

def delete_dish(request):
    dish_id = request.POST.get("dish_id"," ")
    dish = Dish.objects.get(id = dish_id)
    details = MenuDetails.objects.get(dish=dish)
    dish.delete()
    details.delete()
    return redirect('manageMenu')


def browse_restaurants(request):
    restaurants = Restaurants.objects.all()
    args = {'restaurants':restaurants}
    return render(request,'OrderManagement/browseRestaurants.html',args)

def restaurant_page(request,id):
    restaurant = Restaurants.objects.get(id = id)
    menu = Menu.objects.filter(restaurant = restaurant)[0]
    details = MenuDetails.objects.filter(menu = menu)
    args = {'restaurant':restaurant,'details':details}
    cart = request.session.get('cart',{})
    return render(request,"OrderManagement/restaurantPage.html",args)

def add_to_cart(request):
    dish_id = request.POST.get("dish_id"," ")
    restaurant_id = request.POST.get("restaurant_id"," ")
    cart = request.session.get('cart',{})
    if "restaurant_id" in cart:
        if cart["restaurant_id"] != restaurant_id:
            cart = {}
    cart["restaurant_id"] = restaurant_id
    cart[dish_id] = cart.get(dish_id,0) + 1
    request.session['cart'] = cart 
    return redirect("restaurantPage",restaurant_id)

def place_order(request):
    cart = request.session.get('cart',{})
    items = []
    print(cart)
    
    for key,value in cart.items():
        if key == "restaurant_id":
            restaurant_id = value
        else:
            dish = Dish.objects.get(id = key)
            items.append((dish,value))

    restaurant = Restaurants.objects.get(id = restaurant_id)

    args = {"restaurant":restaurant,"items":items}
    return render(request,"OrderManagement/placeOrder.html",args)