# Generated by Django 4.2.5 on 2023-10-14 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_rename_staff_employeeassociation_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='task_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='my_app.taskcategory'),
        ),
    ]
