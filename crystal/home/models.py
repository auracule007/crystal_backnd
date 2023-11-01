from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
from django.utils import timezone
from django.utils.timezone import now 

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(default='')
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Category'

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(default="")
    stockImg = models.ImageField(upload_to = "Product", default="product.jpg")
    stockPrice = models.IntegerField()
    discountedPrice = models.FloatField(null=True, blank=True)
    stockQuantity = models.IntegerField()
    maxQuantity = models.IntegerField(null=True, blank=True)
    minQuantity = models.IntegerField(null=True, blank=True)
    shortDescription = models.TextField(null=True, blank=True)
    longDescription = models.TextField(null=True, blank=True)
    uploaded = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    pix = models.ImageField(upload_to="Profile", default="default_icon.jpg")
    address = models.TextField()
    phone = models.CharField(max_length=50, default='')
    state = models.CharField(max_length= 200)
    city = models.CharField(max_length= 200)
    
    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'profile'
        managed = True
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'

class Shopcart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=1)
    paid = models.BooleanField(default=False)
    size = models.CharField(default='', max_length=100)
    color = models.CharField(default='', max_length=100)
    order_no = models.UUIDField(default=uuid4)
    amount = models.IntegerField()
    quantity = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name
    
class Reviews(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='reviews')
    pix = models.ImageField(upload_to='Reviews', default="default_icon.jpg")
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reviews by {self.name} on {self.product}'
    