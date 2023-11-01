from django.contrib import admin
from . models import *
from django.contrib.admin import ModelAdmin

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'description']
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'name', 'slug', 'stockImg', 'stockPrice', 'discountedPrice', 'stockQuantity', 'maxQuantity', 'minQuantity', 'shortDescription', 'longDescription', 'uploaded']
    search_fields = ['name', 'category', 'slug']
admin.site.register(Product, ProductAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'last_name', 'email', 'pix', 'address', 'state', 'city']
admin.site.register(Profile, ProfileAdmin)

class ShopcartAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'user','name', 'price', 'paid', 'size', 'color','order_no', 'amount', 'quantity', 'date_created', 'date_updated']
    search_fields = ['product', 'user','date_created', 'name']
admin.site.register(Shopcart, ShopcartAdmin)