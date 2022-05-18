from django.db import models
from django.forms import CharField


class Product_type(models.Model):
    product_type = models.CharField(max_length=200, unique=True)

    def __str__(self) -> str:
        return self.product_type


class Product_size(models.Model):
    product_size = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.product_size


class Product(models.Model):
    product_name = models.TextField(max_length=200)
    
    image = models.ImageField(upload_to="images/")
    price = models.IntegerField()
    froduct_for_male = models.BooleanField()
    product_type = models.ForeignKey(Product_type, on_delete=models.CASCADE)
    product_size = models.ManyToManyField(Product_size)

    def __str__(self):
        return self.product_name


class User(models.Model):
    user_name = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    phone = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    full_name = models.CharField(max_length=200)

    def __str__(self):
        return self.user_name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_name_receive = models.CharField(max_length=200)
    phone_receive = models.CharField(max_length=200)
    address_receive = models.CharField(max_length=200)
    sum_price = models.IntegerField()

    def __str__(self):
        return self.user_name_receive


class Cart_item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_size = models.ForeignKey(Product_size, on_delete=models.CASCADE)
    number_product = models.IntegerField()
    sum_price = models.IntegerField()

    def __str__(self):
        return self.product.product_name


class Order_item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_size = models.ForeignKey(Product_size, on_delete=models.CASCADE)
    number_product = models.IntegerField()
    sum_price = models.IntegerField()

    def __str__(self):
        return self.product.product_name
