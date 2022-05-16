from django.urls import path

from . import views

app_name = 'clothes'
urlpatterns = [
    path('', views.home, name='home'),
    path('home/<str:type>/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
]
