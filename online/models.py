from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Product(models.Model):
    # embed_code = models.TextField()
    title = models.CharField(max_length=50) 
    img = models.ImageField(upload_to='images/Product')   
    description = models.TextField()
    price = models.IntegerField()
    rating = models.PositiveIntegerField(verbose_name='Рейтинг')
    sale = models.PositiveIntegerField(default = 0)
    quantily = models.PositiveIntegerField()
    is_available = models.BooleanField(default = True)
    # title, img, description, price, rating, sale, quantily, is_available
    # price = models.PositiveIntegerField()
    
    def __str__(self):
        return self.title

class Order(models.Model):
    adress = models.TextField()
    creаted = models.DateTimeField(auto_now_add=True)
    # adress, created
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)