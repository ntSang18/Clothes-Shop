from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404
from .models import Product_adapter, Product_size, Product_type, User, Product


def home(request, type=""):
    # Create session type_list
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
            if 'user_id' not in request.session:
                request.session['user_id'] = new_user.id
            request.session.modified = True
            return home(request)
        except IntegrityError as e:
            context = {
                "message": "user name, phone number or email already exists..."}
            return render(request, 'clothes/404.html', context=context)
    else:
        return render(request, 'clothes/register.html')


def login(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['password']
        user = User.objects.filter(user_name=user_name, password=password)
        if user.count() == 1:
            return home(request)
        else:
            context = {
                "message": "User name or password incorrect"}
            return render(request, 'clothes/404.html', context=context)
    else:
        return render(request, 'clothes/login.html')


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request=request, template_name='clothes/product_detail.html', context={'product': product})


def add_to_cart(request, product_id, size_id, number):
    product = get_object_or_404(Product, pk=product_id)
    product_size = get_object_or_404(Product_size, pk=size_id)
    product_adapter = Product_adapter(
        product=product, product_size=product_size, number_product=number)
    product_adapter.save()
    user = get_object_or_404(User, pk=request.session['user_id'])
    user.cart.add(product_adapter)
