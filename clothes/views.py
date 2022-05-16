from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product_adapter, Product_size, Product_type, User, Product
from django.contrib import messages


def home(request, type=""):
    # Create session type_list
    if 'user_id' not in request.session:
        request.session['user_id'] = -1
    if 'user_name' not in request.session:
        request.session['user_name'] = ""
    request.session.modified = True
    if 'type_list' not in request.session:
        request.session['type_list'] = []
        type_list = Product_type.objects.all()
        for type in type_list:
            request.session['type_list'].insert(0, type.product_type)
    request.session.modified = True

    if type == "":
        product_list = Product.objects.all()
        context = {
            'product_list': product_list,
        }
    else:
        product_type = get_object_or_404(Product_type, product_type=type)
        product_list = product_type.product_set.all()
        context = {
            'product_list': product_list,
        }
    return render(request, template_name='clothes/home.html', context=context)


def register(request):
    if request.method == 'POST':
        new_user = User()
        new_user.user_name = request.POST['user_name']
        new_user.password = request.POST['password']
        new_user.phone = request.POST['phone']
        new_user.email = request.POST['email']
        new_user.full_name = request.POST['full_name']
        try:
            new_user.save()
            request.session['user_id'] = new_user.id
            request.session['user_name'] = new_user.user_name
            request.session.modified = True
            return redirect('clothes:home')
        except IntegrityError as e:
            messages.success(
                request, ("user name, phone number or email address already exits!"))
            return redirect('clothes:register')
    else:
        return render(request, 'clothes/register.html')


def login(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['password']
        try:
            user = User.objects.get(user_name=user_name, password=password)
            request.session['user_id'] = user.id
            request.session['user_name'] = user.user_name
            request.session.modified = True
            return redirect('clothes:home')
        except:
            messages.success(request, ("user name or password incorrect!"))
            return redirect('clothes:login')
    else:
        return render(request, 'clothes/login.html')


def logout(request):
    request.session['user_id'] = -1
    return redirect('clothes:home')


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request=request, template_name='clothes/product_detail.html', context={'product': product})


def add_to_cart(request):
    product_id = request.POST['product_id']
    size_id = request.POST['size_id']
    number = request.POST['number']

    product = get_object_or_404(Product, pk=product_id)
    product_size = get_object_or_404(Product_size, pk=size_id)
    product_adapter = Product_adapter(
        product=product, product_size=product_size, number_product=number)
    product_adapter.save()
    user = get_object_or_404(User, pk=request.session['user_id'])
    user.cart.add(product_adapter)
    return redirect('clothes:product_detail', product_id=product_id)
