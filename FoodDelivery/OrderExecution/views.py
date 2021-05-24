from django.shortcuts import render
from django.shortcuts import redirect
from OrderExecution.models import OrderDetails,Order,Status
from django.http import HttpResponse
from OrderManagement.models import Dish
import geopy.distance
from Users.models import Customers,Restaurants,Deliverers,DelivererStatus
import datetime
import threading,time
import json 


def place_order(request):
    cart = request.session.get('cart',{})
    customer = Customers.objects.get(user = request.user)
    restaurant_id = cart.get("restaurant_id",-1)
    restaurant = Restaurants.objects.get(id = restaurant_id)
    now = datetime.datetime.now()
    order = Order(status = Status.PENDING_RESTAURANT,customer = customer,restaurant = restaurant,date = now)
    order.save()

    price = 0
    for key,value in cart.items():
        if key != "restaurant_id":
            dish = Dish.objects.get(id = key)
            orderDetail = OrderDetails(dish = dish,order = order,quantity = value)
            orderDetail.save()
            price+= dish.price * value

    order.price = price
    order.save()
    cart.clear()
    request.session['cart'] = cart 
    return redirect("yourOrder")

def your_order(request):
        customer = Customers.objects.get(user = request.user) 
        orders = Order.objects.filter(customer= customer)
        args = {"orders":orders}
        return render(request,"OrderExecution/yourOrder.html",args)

def find_deliverer(order,excluded = None):
        def dist(r_lat, r_lng, d_lat, d_lng):
                return geopy.distance.geodesic((r_lat,r_lng), (d_lat,d_lng))


        restaurant = order.restaurant
        restaurant_latitude = restaurant.latitude
        restaurant_longitude = restaurant.longitude
        min_dist = float("inf")
        for deliverer in Deliverers.objects.all():
                if deliverer.status == DelivererStatus.AVAILABLE and deliverer != excluded:
                        curr_dist = dist(restaurant_latitude,restaurant_longitude,deliverer.latitude,deliverer.longitude)
                        if  curr_dist < min_dist:
                                min_dist = curr_dist
                                closest_deliverer = deliverer
        return closest_deliverer


def check_expiration(order):
        time.sleep(120)
        if order.status == Status.PENDING_DELIVERY:
                order.status = Status.DECLINED
                order.save()

def accept_order_r(request):
        order_id = request.POST.get("order_id"," ")
        order = Order.objects.get(id = order_id)
        order.deliverer = find_deliverer(order)
        thread = threading.Thread(target = check_expiration,args=(order,))
        thread.start()
        order.status = Status.PENDING_DELIVERY
        order.save()
        return redirect("pendingOrders")

def decline_order_r(request):
        order_id = request.POST.get("order_id"," ")
        order = Order.objects.get(id = order_id)
        order.status = Status.DECLINED
        order.save()
        return redirect("pendingOrders")


def pending_orders(request):
        restaurant = Restaurants.objects.get(user = request.user)
        pending_orders = Order.objects.filter(restaurant= restaurant)
        args = {"orders":pending_orders}
        return render(request,"OrderExecution/pendingOrders.html",args)

def accept_order_d(request):
        order_id = request.POST.get("order_id"," ")
        order = Order.objects.get(id = order_id)
        order.status = Status.INPROGRESS
        order.save()
        deliverer = Deliverers.objects.get(user = request.user)
        deliverer.status = DelivererStatus.BUSY
        deliverer.save()

        to_change = Order.objects.filter(deliverer = deliverer)

        for order_to_change in to_change:
            if order_to_change != order:
                order_to_change.deliverer = find_deliverer(order)
                order_to_change.status = Status.PENDING_DELIVERY
                order_to_change.save()

        return redirect("orderDelivery")

def decline_order_d(request):
        deliverer = Deliverers.objects.get(user = request.user)
        order_id = request.POST.get("order_id"," ")
        order = Order.objects.get(id = order_id)
        order.deliverer = find_deliverer(order,excluded =deliverer)
        order.save()
        return redirect("orderDelivery")
        
        
        
def order_delivery(request):
        deliverer = Deliverers.objects.get(user = request.user)
        pending_orders = Order.objects.filter(deliverer = deliverer)
        args = {"orders":pending_orders}
        return render(request,"OrderExecution/orderDelivery.html",args)

def complete_order(request):
        order_id = request.POST.get("order_id"," ")
        order = Order.objects.get(id = order_id)
        order.status = Status.COMPLETED
        order.save()
        deliverer = Deliverers.objects.get(user = request.user)
        deliverer.status = DelivererStatus.AVAILABLE
        deliverer.save()
        return redirect("orderDelivery")


def update_location(request):
        deliverer = Deliverers.objects.get(user = request.user)
        latitude = request.POST.get('latitude', None)
        longitude = request.POST.get('longitude', None)
        deliverer.latitude = latitude
        deliverer.longitude = longitude
        deliverer.save()
        return HttpResponse(json.dumps({'status': "OK"}), content_type="application/json")    



        
    




