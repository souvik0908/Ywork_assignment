from django.urls import path
from .views import (
    order_list, create_order,get_token
)

urlpatterns = [
    path('orders/', order_list, name='order-list'),
    path('orders/create/', create_order, name='order-create'),
    path('get-token/', get_token, name='get-token'),
]
