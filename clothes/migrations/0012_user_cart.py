# Generated by Django 4.0.4 on 2022-05-15 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0011_rename_productsize_product_size_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cart',
            field=models.ManyToManyField(to='clothes.product'),
        ),
    ]
