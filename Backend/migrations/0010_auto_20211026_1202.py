# Generated by Django 3.2.8 on 2021-10-26 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0009_auto_20211026_1147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='album',
        ),
        migrations.AddField(
            model_name='album',
            name='model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Backend.plant'),
        ),
    ]