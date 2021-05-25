from django.urls import path
from OrderExecution import views as OrderExecution_views



urlpatterns = [
    path("placeOrder/",OrderExecution_views.place_order,name="placeOrder"),
    path("pendingOrders/",OrderExecution_views.pending_orders,name="pendingOrders"),
    path('acceptOrderR/',OrderExecution_views.accept_order_r,name ="acceptOrderR"),
    path('acceptOrderD/',OrderExecution_views.accept_order_d,name ="acceptOrderD"),
    path("orderDelivery/",OrderExecution_views.order_delivery,name="orderDelivery"),
    path("completeOrder/",OrderExecution_views.complete_order,name ="completeOrder"),
    path("yourOrder/",OrderExecution_views.your_order,name = "yourOrder"),
    path("declineOrderR/",OrderExecution_views.decline_order_r,name="declineOrderR"),
    path("declineOrderD/",OrderExecution_views.decline_order_d,name = "declineOrderD"),
    path("profile/updateLocation/",OrderExecution_views.update_location,name ="updateLocation"), 
    path("rateRestaurant/",OrderExecution_views.rate_restaurant,name = "rateRestaurant"),
    path("rateDeliverer",OrderExecution_views.rate_deliverer,name = "rateDeliverer")
]



