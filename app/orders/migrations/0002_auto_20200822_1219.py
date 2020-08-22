# Generated by Django 3.1 on 2020-08-22 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('In Cart', 'In Cart'), ('Ordered', 'Ordered'), ('Fulfilled', 'Fulfilled'), ('Completed', 'Completed')], default='In Cart', max_length=9),
        ),
    ]
