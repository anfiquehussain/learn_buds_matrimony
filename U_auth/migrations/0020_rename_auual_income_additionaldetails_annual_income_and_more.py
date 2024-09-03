# Generated by Django 5.0.8 on 2024-09-02 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('U_auth', '0019_disabilities_alter_additionaldetails_auual_income_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='additionaldetails',
            old_name='auual_income',
            new_name='annual_income',
        ),
        migrations.RenameField(
            model_name='additionaldetails',
            old_name='user_disabilitys',
            new_name='user_disabilities',
        ),
        migrations.RemoveField(
            model_name='additionaldetails',
            name='is_married',
        ),
        migrations.AddField(
            model_name='additionaldetails',
            name='married_status',
            field=models.CharField(choices=[('single', 'Single'), ('divorced', 'Divorced'), ('widowed', 'Widowed')], default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='additionaldetails',
            name='family_type',
            field=models.CharField(choices=[('joint', 'Joint'), ('nuclear', 'Nuclear'), ('extended', 'Extended')], max_length=50),
        ),
    ]
