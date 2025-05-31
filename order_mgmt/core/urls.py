from django.urls import path
from . import views

urlpatterns = [
    path('oauth2callback/', views.GoogleOAuthCallback.as_view(), name='google-oauth-callback'),
    path('orders/create/', views.create_order, name='create-order'),
    path('orders/', views.order_list, name='list-orders'),
]
