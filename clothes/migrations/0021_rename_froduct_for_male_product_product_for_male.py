# Generated by Django 4.0.4 on 2022-05-19 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0020_cart_item_order_item_delete_product_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='froduct_for_male',
            new_name='product_for_male',
        ),
    ]