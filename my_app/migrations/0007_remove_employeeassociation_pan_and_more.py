# Generated by Django 4.2.5 on 2023-10-14 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_alter_employee_managers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeeassociation',
            name='PAN',
        ),
        migrations.RemoveField(
            model_name='employeeassociation',
            name='address',
        ),
        migrations.RemoveField(
            model_name='employeeassociation',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='employeeassociation',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='employee',
            name='PAN',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
