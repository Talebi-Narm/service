# Generated by Django 3.2.8 on 2021-10-26 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0011_auto_20211026_1209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='default',
        ),
    ]