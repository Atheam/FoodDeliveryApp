from FoodDelivery.settings import ACCEPT_TIME
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
    customer = Customers.objects.filter(user = request.user).first()
    restaurant_id = cart.get("restaurant_id",-1)
    restaurant = Restaurants.objects.filter(id = restaurant_id).first()

    if customer and restaurant:
        now = datetime.datetime.now()
        order = Order(status = Status.PENDING_RESTAURANT,customer = customer,restaurant = restaurant,date = now)
        order.save()

        price = 0
        for key,quantity in cart.items():
            if key != "restaurant_id":
                dish = Dish.objects.filter(id = key).first()
                orderDetail = OrderDetails(dish = dish,order = order,quantity = quantity)
                orderDetail.save()
                price+= dish.price * quantity
        order.price = price
        order.save()
        cart.clear()
        request.session['cart'] = cart
    return redirect("yourOrder")

def your_order(request):
        customer = Customers.objects.filter(user = request.user).first()
        orders = Order.objects.filter(customer= customer)[::-1]
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

def check_expiration(order_id):
        time.sleep(ACCEPT_TIME)
        order = Order.objects.filter(id = order_id).first()
        if order and order.status == Status.PENDING_DELIVERY:
                order.status = Status.DECLINED
                order.deliverer.status = DelivererStatus.AVAILABLE
                order.save()

def accept_order_r(request):
        order_id = request.POST.get("order_id"," ")
        order = Order.objects.filter(id = order_id).first()
        order.deliverer = find_deliverer(order)
        order.status = Status.PENDING_DELIVERY
        thread = threading.Thread(target = check_expiration,args=(order_id,))
        thread.start()
        order.save()
        return redirect("pendingOrders")

def decline_order_r(request):
        order_id = request.POST.get("order_id"," ")
        order = Order.objects.filter()(id = order_id).first()
        order.status = Status.DECLINED
        order.save()
        return redirect("pendingOrders")

def accept_order_d(request):
        order_id = request.POST.get("order_id"," ")
        order = Order.objects.filter(id = order_id).first()
        order.status = Status.INPROGRESS
        order.save()
        deliverer = Deliverers.objects.filter(user = request.user).first()
        deliverer.status = DelivererStatus.BUSY
        deliverer.save()

        to_change = Order.objects.filter(deliverer = deliverer,status=Status.PENDING_DELIVERY)

        for order_to_change in to_change:
            if order_to_change != order:
                order_to_change.deliverer = find_deliverer(order)
                order_to_change.save()

        return redirect("orderDelivery")

def decline_order_d(request):
        deliverer = Deliverers.objects.filter(user = request.user).first()
        order_id = request.POST.get("order_id"," ")
        order = Order.objects.filter(id = order_id).first()
        order.deliverer = find_deliverer(order,excluded =deliverer)
        order.save()
        return redirect("orderDelivery")


def pending_orders(request):
        restaurant = Restaurants.objects.filter(user = request.user).first()
        if restaurant:
                pending_orders = Order.objects.filter(restaurant= restaurant,status = Status.PENDING_RESTAURANT)
                order_details = OrderDetails.objects.filter(order__in = pending_orders)
                args = {"orders":pending_orders,"details":order_details,"accepted":True}
        else:
                args = {"accepted":False}
        return render(request,"OrderExecution/pendingOrders.html",args)
        
        
def order_delivery(request):
        deliverer = Deliverers.objects.filter(user = request.user).first()
        if deliverer:
                pending_orders = Order.objects.filter(deliverer= deliverer)
                order_details = OrderDetails.objects.filter(order__in = pending_orders)
                args = {"orders":pending_orders,"details":order_details,"accepted": True}
        else:
                args = {"accepted":False}
        return render(request,"OrderExecution/orderDelivery.html",args)

def complete_order(request):
        order_id = request.POST.get("order_id"," ")
        order = Order.objects.filter(id = order_id).first()
        order.status = Status.COMPLETED
        order.save()
        deliverer = Deliverers.objects.filter(user = request.user).first()
        deliverer.status = DelivererStatus.AVAILABLE
        deliverer.save()
        return redirect("orderDelivery")

def update_location(request):
        deliverer = Deliverers.objects.filter(user = request.user).first()
        latitude = request.POST.get('latitude', None)
        longitude = request.POST.get('longitude', None)
        deliverer.latitude = latitude
        deliverer.longitude = longitude
        deliverer.save()
        return HttpResponse(json.dumps({'status': "OK"}), content_type="application/json")    

def rate_restaurant(request):
        order_id = request.POST.get("order_id"," ")
        rate = int(request.POST.get("rate", " "))
        order = Order.objects.filter(id = order_id).first()
        order.restaurant_rating = rate
        order.save()

        restaurant = order.restaurant
        restaurant.rate_count +=1
        restaurant.rate_sum += rate
        restaurant.rating = float(restaurant.rate_sum)/restaurant.rate_count
        restaurant.save()
        return redirect("yourOrder")

def rate_deliverer(request):
        order_id = request.POST.get("order_id"," ")
        rate = int(request.POST.get("rate", " "))
        order = Order.objects.filter(id = order_id).first()
        order.deliverer_rating = rate
        order.save()

        deliverer = order.deliverer
        deliverer.rate_count +=1
        deliverer.rate_sum += rate
        deliverer.rating =  float(deliverer.rate_sum)/deliverer.rate_count
        deliverer.save()
        return redirect("yourOrder")




        
    




