# Generated by Django 4.1.7 on 2023-03-09 09:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpecilistFields',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_code', models.CharField(blank=True, max_length=150, verbose_name='id_code')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='birth_date')),
                ('degree', models.CharField(blank=True, choices=[('Associate', 'Associate'), ('Bachelor', 'Bachelor'), ('Master', 'Master'), ('Doctoral', 'Doctoral')], max_length=50, null=True, verbose_name='degree')),
                ('major', models.CharField(blank=True, max_length=150, verbose_name='major')),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+## ### ### ####'. Up to 10 digits allowed.", regex='^(\\+\\d{1,2}\\s?)?1?\\-?\\.?\\s?\\(?\\d{3}\\)?[\\s.-]?\\d{3}[\\s.-]?\\d{4}$')], verbose_name='phone_number')),
                ('about', models.TextField(blank=True, max_length=500, verbose_name='about')),
                ('address', models.TextField(blank=True, max_length=500, verbose_name='address')),
                ('is_online', models.BooleanField(default=True)),
                ('rate', models.IntegerField(default=0, verbose_name='rate')),
            ],
        ),
    ]
