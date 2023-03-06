# Generated by Django 3.2.8 on 2021-10-24 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0012_alter_memberfields_plants_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memberfields',
            name='plants_cart',
        ),
        migrations.RemoveField(
            model_name='memberfields',
            name='tools_cart',
        ),
        migrations.AddField(
            model_name='memberfields',
            name='address',
            field=models.TextField(blank=True, max_length=500, verbose_name='address'),
        ),
    ]