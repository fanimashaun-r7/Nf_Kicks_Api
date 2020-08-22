# Generated by Django 3.1 on 2020-08-22 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200822_1219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='ordered_date',
        ),
        migrations.AddField(
            model_name='order',
            name='stripe_charge_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='refund_status',
            field=models.CharField(choices=[('None', 'None'), ('Requested', 'Requested'), ('Granted', 'Granted')], default='None', max_length=9),
        ),
    ]