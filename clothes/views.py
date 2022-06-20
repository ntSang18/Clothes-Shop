from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from .models import Cart_item, Product_size, Product_type, User, Product, Order, Order_item
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

    if request.method == 'POST':
        search = request.POST['search']
        product_list = Product.objects.filter(product_name__contains=search)
        context = {
            'product_list': product_list,
        }
    else:
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
            messages.error(
                request, ("User name, phone number or email address already exits!"))
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
            messages.error(request, ("User name or password incorrect!"))
            return redirect('clothes:login')
    else:
        return render(request, 'clothes/login.html')


def logout(request):
    request.session['user_id'] = -1
    return redirect('clothes:home')


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request=request, template_name='clothes/product_detail.html', context={'product': product})


def add_cart_item(request):
    product_id = request.POST['product_id']
    size_id = request.POST['size_id']
    number = request.POST['number']

    if request.session['user_id'] != -1:
        user = get_object_or_404(User, pk=request.session['user_id'])
        # cart_list = user.cart_item_set.all()
        # for item in cart_list:
        #     if item.product.id == product_id and item.product_size.id == size_id:
        #         item.number_product += number
        #         item.save()
        #         break
        # else:
        product = get_object_or_404(Product, pk=product_id)
        product_size = get_object_or_404(Product_size, pk=size_id)
        sum_price = product.price * int(number)
        cart_item = Cart_item(
            product=product, user=user, product_size=product_size, number_product=number, sum_price=sum_price)
        cart_item.save()
        messages.success(
            request, ("Thêm vào giỏ hàng thành công."))
        return redirect('clothes:product_detail', product_id=product_id)


def del_cart_item(request, product_item_id):
    Cart_item.objects.get(pk=product_item_id).delete()
    return redirect('clothes:cart_view')


def cart_view(request):
    if request.session['user_id'] != -1:
        user = User.objects.get(pk=request.session['user_id'])
        cart_list = user.cart_item_set.all()
        context = {
            'cart_list': cart_list,
        }
        return render(request, template_name='clothes/cart.html', context=context)
    else:
        return redirect('clothes:login')


def order_view(request, item_id=-1):
    if request.session['user_id'] != -1:
        user = User.objects.get(pk=request.session['user_id'])
        if item_id == -1:
            product_id = request.POST['product_id']
            size_id = request.POST['size_id']
            number = request.POST['number']
            product = get_object_or_404(Product, pk=product_id)
            product_size = get_object_or_404(Product_size, pk=size_id)
            sum_price = product.price * int(number)
            order_item = Order_item(
                product=product, product_size=product_size, number_product=number, sum_price=sum_price)
            context = {
                'order_item': order_item,
                'user': user
            }
        else:
            order_item = Cart_item.objects.get(pk=item_id)
            context = {
                'order_item': order_item,
                'user': user
            }
        return render(request, template_name='clothes/order.html', context=context)
    else:
        return redirect('clothes:login')


def order(request):
    if request.session['user_id'] != -1:
        user = User.objects.get(pk=request.session['user_id'])
        user_name_receive = request.POST['user_name_receive']
        address_receive = request.POST['address_receive']
        phone_receive = request.POST['phone_receive']
        product_id = request.POST['product_id']
        size = request.POST['product_size']
        number_product = request.POST['number_product']
        product = get_object_or_404(Product, pk=product_id)
        product_size = get_object_or_404(Product_size, product_size=size)
        sum_price = product.price * int(number_product)
        order = Order(user=user, user_name_receive=user_name_receive,
                      phone_receive=phone_receive, address_receive=address_receive, sum_price=sum_price)
        order.save()
        order_item = Order_item(
            product=product, order=order, product_size=product_size, number_product=number_product, sum_price=sum_price)
        order_item.save()
        messages.success(request, "Đặt hàng thành công.")
        return redirect('clothes:home')
    else:
        return redirect('clothes:login')
