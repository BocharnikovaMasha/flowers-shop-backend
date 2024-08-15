from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('catalog/', catalog, name='catalog'),
    path('orders/', orders, name='orders'),
    path('order_create/', order_create, name='order_create'),
    path('details/<int:product_id>', details, name='details'),
]
