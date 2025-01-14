# Generated by Django 4.2 on 2023-04-21 19:58

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToolComment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('text', models.TextField()),
                ('rate', models.IntegerField(help_text='enter integer between 1 and 5!', validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('is_buyer', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('reply_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.toolcomment')),
                ('tool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.tool')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PlantComment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('text', models.TextField()),
                ('rate', models.IntegerField(help_text='enter integer between 1 and 5!', validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('is_buyer', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.plant')),
                ('reply_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.plantcomment')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
