# Generated by Django 5.0.8 on 2024-09-02 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('U_auth', '0017_userextradetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinterests',
            name='interests',
        ),
        migrations.RemoveField(
            model_name='userinterests',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userqualification',
            name='qualifications',
        ),
        migrations.RemoveField(
            model_name='userqualification',
            name='user',
        ),
        migrations.AddField(
            model_name='userpersonaldetails',
            name='hobbies',
            field=models.ManyToManyField(to='U_auth.hobbies'),
        ),
        migrations.AddField(
            model_name='userpersonaldetails',
            name='interests',
            field=models.ManyToManyField(to='U_auth.interests'),
        ),
        migrations.AddField(
            model_name='userpersonaldetails',
            name='qualifications',
            field=models.ManyToManyField(to='U_auth.qualifications'),
        ),
        migrations.DeleteModel(
            name='UserHobbies',
        ),
        migrations.DeleteModel(
            name='UserInterests',
        ),
        migrations.DeleteModel(
            name='UserQualification',
        ),
    ]
