# Generated by Django 4.2.1 on 2023-07-07 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_initial'),
        ('order', '0007_alter_order_coupon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='plants',
            field=models.ManyToManyField(blank=True, to='cart.plantcart'),
        ),
        migrations.AlterField(
            model_name='order',
            name='tools',
            field=models.ManyToManyField(blank=True, to='cart.toolcart'),
        ),
    ]
