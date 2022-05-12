from django.db import models


class Account(models.Model):
    user_name = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.user_name


class User(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    gender = models.BooleanField
    birthday = models.DateField
    email = models.EmailField

    def __str__(self):
        return self.full_name
