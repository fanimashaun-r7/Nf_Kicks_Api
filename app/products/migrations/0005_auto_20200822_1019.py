# Generated by Django 3.1 on 2020-08-22 10:19

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200822_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='slug',
            field=models.SlugField(blank=True, default='hello-world', editable=False, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), 'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.', 'invalid')]),
            preserve_default=False,
        ),
    ]
