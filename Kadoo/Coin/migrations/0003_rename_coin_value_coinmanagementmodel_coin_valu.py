# Generated by Django 3.2.8 on 2021-12-13 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Coin', '0002_auto_20211213_1049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coinmanagementmodel',
            old_name='coin_value',
            new_name='coin_valu',
        ),
    ]
