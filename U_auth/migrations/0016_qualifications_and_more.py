# Generated by Django 5.0.8 on 2024-09-01 06:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('U_auth', '0015_interests_remove_hobbies_user_userhobbies_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qualifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='userpersonaldetails',
            name='qualification',
        ),
        migrations.CreateModel(
            name='UserQualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualifications', models.ManyToManyField(to='U_auth.qualifications')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_qualifications', to='U_auth.userpersonaldetails')),
            ],
        ),
    ]