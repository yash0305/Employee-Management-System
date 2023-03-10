# Generated by Django 4.1.5 on 2023-01-14 14:15

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(blank=True, max_length=13, validators=[django.core.validators.RegexValidator(message='Mobile number should contain 10 digits', regex='^\\+?91?\\d{10}$')])),
                ('salary', models.IntegerField(default=0)),
                ('bonus', models.IntegerField(default=0)),
                ('experienceInYears', models.IntegerField(default=0)),
                ('hireDate', models.DateField()),
                ('jobRole', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.role')),
            ],
        ),
    ]
