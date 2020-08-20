# Generated by Django 3.1 on 2020-08-20 19:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200820_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=120, unique=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(120)]),
        ),
        migrations.AlterField(
            model_name='size',
            name='size',
            field=models.FloatField(choices=[(3, '3'), (4, '4'), (6, '6'), (6.5, '6.5'), (7, '7'), (7.5, '7.5'), (8, '8'), (8.5, '8.5'), (9, '9'), (9.5, '9.5'), (10, '10'), (10.5, '10.5'), (11, '11'), (11.5, '11.5'), (12, '12'), (12.5, '12.5'), (13, '13')], validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000)]),
        ),
    ]
