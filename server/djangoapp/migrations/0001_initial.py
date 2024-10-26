# Generated by Django 5.1.2 on 2024-10-26 17:17

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarMake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('SEDAN', 'Sedan'), ('SUV', 'SUV'), ('WAGON', 'Wagon')], max_length=10)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(2015), django.core.validators.MaxValueValidator(2023)])),
                ('car_make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoapp.carmake')),
            ],
        ),
    ]
