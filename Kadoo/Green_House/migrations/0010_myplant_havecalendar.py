# Generated by Django 3.2.8 on 2022-01-24 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Green_House', '0009_auto_20211228_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='myplant',
            name='haveCalendar',
            field=models.BooleanField(default=False),
        ),
    ]
