# Generated by Django 5.0.8 on 2024-09-28 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matrimony_admin', '0009_subscription_subscription_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='subscription_type',
        ),
    ]
