from django.shortcuts import render, redirect
from .models import Product
from .models import Order

# Create your views here.

def home(request):
    return render(request, 'online/index.html') 

def catalog(request):
     archive = Product.objects.all()
     # archive = Product.objects.last()
     # archive = Product.objects.first()
     return render(request, 'online/catalog.html', {'posts': archive})
     
# def playlist(request):
#     archive = Video.objects.all()
#     return render(request, 'playlist/playlist.html', {'posts': archive}) 

def orders(request):
     archive = Order.objects.all()
     for order in archive:
          print(order.creаted)
     return render(request, 'online/orders.html', {'posts': archive})

def order_create(request, product_id):
     product = Product.objects.get(id=product_id) 
     if request.method == 'POST':
          adress=request.POST['adress']
          Order.objects.create(adress=adress, product=product)
          return redirect('orders')
     return render(request, 'online/order_create.html')

def details(request, product_id):
     product = Product.objects.get(id=product_id) 
     return render(request, 'online/details.html', {'product': product})