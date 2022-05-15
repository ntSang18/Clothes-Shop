from django.urls import path

from . import views

app_name = 'clothes'
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('<int:product_id>/', views.product_detail, name='product_detail')
]
