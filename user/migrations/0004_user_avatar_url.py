# Generated by Django 4.2.1 on 2023-06-05 14:50

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_merge_0002_delete_specialist_0002_user_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar_url',
            field=models.ImageField(blank=True, null=True, upload_to=user.models.upload_to),
        ),
    ]