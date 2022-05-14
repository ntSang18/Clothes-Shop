from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=200, unique=True)
    passworld = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    full_name = models.CharField(max_length=200)

    def __str__(self):
        return self.user_name


class Product_type(models.Model):
    product_type = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.product_type


class Product(models.Model):
    product_name = models.TextField(max_length=200)
    image = models.ImageField(upload_to="images/")
    price = models.IntegerField()
    froduct_for_male = models.BooleanField()
    product_type = models.ForeignKey(Product_type, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name
