# Generated by Django 5.0.8 on 2024-08-29 08:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('U_auth', '0010_alter_additionaldetails_is_married'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship_goals',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
