from django.contrib import admin
from .models import User, Product, Product_type, Product_size, Cart_item, Order_item, Order

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Product_type)
admin.site.register(Product_size)
admin.site.register(Cart_item)
admin.site.register(Order_item)
admin.site.register(Order)
