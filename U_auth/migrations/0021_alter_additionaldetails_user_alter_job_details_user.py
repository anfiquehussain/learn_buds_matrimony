# Generated by Django 5.0.8 on 2024-09-02 08:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('U_auth', '0020_rename_auual_income_additionaldetails_annual_income_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionaldetails',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='job_details',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]