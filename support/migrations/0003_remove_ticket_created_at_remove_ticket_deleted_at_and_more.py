# Generated by Django 4.2.1 on 2023-06-04 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0002_remove_specialist_is_busy_alter_specialist_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='updated_at',
        ),
    ]