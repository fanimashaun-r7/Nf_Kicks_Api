# Generated by Django 3.1 on 2020-08-19 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20200819_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('I', 'In Cart'), ('O', 'Ordered'), ('F', 'Fulfilled'), ('C', 'Completed')], default='I', max_length=2),
        ),
    ]
