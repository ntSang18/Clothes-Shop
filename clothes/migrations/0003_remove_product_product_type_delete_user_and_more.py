# Generated by Django 4.0.4 on 2022-05-14 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0002_product_product_type_remove_user_account_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_type',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Product_type',
        ),
    ]