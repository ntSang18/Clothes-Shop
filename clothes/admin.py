from django.contrib import admin
from .models import User, Product, Product_type, Product_size, Product_adapter

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Product_type)
admin.site.register(Product_size)
admin.site.register(Product_adapter)
