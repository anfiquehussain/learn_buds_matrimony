# Generated by Django 5.0.8 on 2024-09-01 11:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('U_auth', '0016_qualifications_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserExtraDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('continent', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('country_code', models.CharField(blank=True, max_length=10, null=True)),
                ('region', models.CharField(blank=True, max_length=100, null=True)),
                ('region_name', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('district', models.CharField(blank=True, max_length=100, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=20, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('lon', models.FloatField(blank=True, null=True)),
                ('timezone', models.CharField(blank=True, max_length=100, null=True)),
                ('currency', models.CharField(blank=True, max_length=10, null=True)),
                ('isp', models.CharField(blank=True, max_length=255, null=True)),
                ('org', models.CharField(blank=True, max_length=255, null=True)),
                ('as_name', models.CharField(blank=True, max_length=255, null=True)),
                ('mobile', models.BooleanField(default=False)),
                ('proxy', models.BooleanField(default=False)),
                ('hosting', models.BooleanField(default=False)),
                ('query_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
