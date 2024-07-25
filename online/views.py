from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'online/index.html') 

def catalog(request):
     return render(request, 'online/catalog.html')
     
def orders(request):
     return render(request, 'online/orders.html')

def order_create(request):
     return render(request, 'online/order_create.html')

