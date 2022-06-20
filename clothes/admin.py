from django.contrib import admin
from numpy import insert
from .models import User, Product, Product_type, Product_size, Cart_item, Order_item, Order


class UserAdmin(admin.ModelAdmin):
    fields = ['user_name', 'phone', 'email', 'full_name']
    readonly_fields = ['user_name', 'phone', 'email', 'full_name']


class OrderItemInline(admin.TabularInline):
    model = Order_item
    extra = 0
    readonly_fields = ['product', 'order',
                       'product_size', 'number_product', 'sum_price']
    can_delete = False


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    readonly_fields = ['user', 'user_name_receive',
                       'phone_receive', 'address_receive', 'sum_price']


admin.site.register(Product)
admin.site.register(Product_type)
admin.site.register(Product_size)
admin.site.register(User, UserAdmin)
admin.site.register(Order, OrderAdmin)
