from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Product)  
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'img', 'description', 'price', 'rating', 'sale', )
    #  'quantily','is_available', 

@admin.register(Order)  
class OrderAdmin(admin.ModelAdmin):
    list_display = ('adress', 'creаted', 'product', )