from hashlib import new
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User


def index(request):
    return render(request, template_name='clothes/index.html')


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
