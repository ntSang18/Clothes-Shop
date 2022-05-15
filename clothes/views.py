from hashlib import new
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User, Product


def home(request):
    product_list = Product.objects.all()
    context = {'product_list': product_list}
    return render(request, template_name='clothes/home.html', context=context)


def register(request):
    if request.method == 'POST':
        # user_name = request.POST['user_name']
        # phone = request.POST['phone']
        # password = request.POST['password']
        # new_account = Account()
        # new_account.user_name = user_name
        # new_account.phone = phone
        # new_account.password = password
        # new_account.save()
        return render(request, 'clothes/index.html')
    else:
        return render(request, 'clothes/register.html')
