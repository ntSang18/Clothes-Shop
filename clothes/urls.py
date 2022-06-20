from django.urls import path

from . import views

app_name = 'clothes'
urlpatterns = [
    path('', views.home, name='home'),
    path('home/<str:type>/', views.home, name='home'),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add_cart_item/', views.add_cart_item, name='add_cart_item'),
    path('del_cart_item/<int:product_item_id>/',
         views.del_cart_item, name='del_cart_item'),
    path('cart_view/', views.cart_view, name='cart_view'),
    path('order_view/', views.order_view, name='order_view'),
    path('order_view/<int:item_id>/', views.order_view, name='order_view'),
    path('order/', views.order, name='order'),
]
