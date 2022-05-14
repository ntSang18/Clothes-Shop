from django.contrib import admin
from .models import User, Product, Product_type

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Product_type)
