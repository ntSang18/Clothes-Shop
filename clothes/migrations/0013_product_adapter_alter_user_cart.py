# Generated by Django 4.0.4 on 2022-05-15 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0012_user_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_adapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_product', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothes.product')),
                ('product_size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothes.product_size')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='cart',
            field=models.ManyToManyField(to='clothes.product_adapter'),
        ),
    ]
