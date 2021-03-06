from django.shortcuts import render
from django.http import HttpResponse
from Users.models import Customers, Restaurants    
from OrderManagement.models import Menu,MenuDetails,Dish  
from OrderManagement.forms import AddDishForm
from django.shortcuts import redirect

def manage_menu(request):
    restaurant = Restaurants.objects.filter(user = request.user).first()
    if restaurant:
        menu = Menu.objects.filter(restaurant = restaurant).first()
        details = MenuDetails.objects.filter(menu = menu)
        args = {'details':details,'accepted':True}
    else:
        args = {'accepted':False}
    return render(request,'OrderManagement/menuManagement.html',args)

def add_dish(request):
    if request.method == "POST":
        form = AddDishForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']
            dish = Dish(name = name,price= price,description=description, image=image)
            dish.save()
            restaurant = Restaurants.objects.filter(user = request.user).first()
            menu = Menu.objects.filter(restaurant = restaurant).first()
            menu_details = MenuDetails(dish = dish,menu = menu)
            menu_details.save()
            return redirect('manageMenu')
    else:
        form = AddDishForm()
    
    return render(request,'OrderManagement/addDish.html',{'form':form})

def delete_dish(request):
    dish_id = request.POST.get("dish_id"," ")
    dish = Dish.objects.fitler(id = dish_id).first()
    details = MenuDetails.objects.filter(dish=dish).first()
    dish.delete()
    details.delete()
    return redirect('manageMenu')


def browse_restaurants(request):
    restaurants = Restaurants.objects.all()
    args = {'restaurants':restaurants}
    return render(request,'OrderManagement/browseRestaurants.html',args)

def restaurant_page(request,id):
    restaurant = Restaurants.objects.filter(id = id).first()
    menu = Menu.objects.filter(restaurant = restaurant).first()
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

def cart_info(request):
    customer = Customers.objects.filter(user = request.user).first()
    
    
    if not customer:
        args ={"accepted":False}
    else:
        cart = request.session.get('cart',{})
        print(cart)
        total = 0
        items = []
        for key,value in cart.items():
            if key == "restaurant_id":
                restaurant_id = value
            else:
                dish = Dish.objects.filter(id = key).first()
                total+=dish.price*value
                items.append((dish,value))

        if items:
            restaurant = Restaurants.objects.filter(id = restaurant_id).first()
            args = {"restaurant":restaurant,"items":items,"total":round(total,2),"empty":False,"accepted":True}
        else:
            args = {"empty":True,"accepted":True}

    
    return render(request,"OrderManagement/cartInfo.html",args)