# Generated by Django 4.1.5 on 2023-01-13 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_employee_experienceinyears'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='phone',
        ),
    ]
