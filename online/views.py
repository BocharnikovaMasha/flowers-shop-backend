from django.shortcuts import render
from .models import Product

# Create your views here.

def home(request):
    return render(request, 'online/index.html') 

def catalog(request):
     archive = Product.objects.all()
     return render(request, 'online/catalog.html', {'posts': archive})
     
# def playlist(request):
#     archive = Video.objects.all()
#     return render(request, 'playlist/playlist.html', {'posts': archive}) 

def orders(request):
     return render(request, 'online/orders.html')

def order_create(request):
     return render(request, 'online/order_create.html')

