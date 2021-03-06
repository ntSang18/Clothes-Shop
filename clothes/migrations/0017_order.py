# Generated by Django 4.0.4 on 2022-05-17 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0016_cart_item_sum_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_product', models.IntegerField()),
                ('sum_price', models.IntegerField()),
                ('user_name_receive', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('address_receive', models.CharField(max_length=200)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothes.product')),
                ('product_size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothes.product_size')),
            ],
        ),
    ]
