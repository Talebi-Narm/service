# Generated by Django 3.2.8 on 2021-10-27 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0015_alter_tool_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=50),
        ),
    ]