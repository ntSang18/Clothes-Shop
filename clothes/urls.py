from django.urls import path

from . import views

app_name = 'clothes'
urlpatterns = [
    path('', views.home, name='home'),
    path('<str:type>/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add_to_cart/<int:product_id>/<int:size_id>/<int:number>/',
         views.add_to_cart, name='add_to_cart'),
]
