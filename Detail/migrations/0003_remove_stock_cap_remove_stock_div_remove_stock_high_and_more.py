# Generated by Django 4.2 on 2023-04-25 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Detail', '0002_stock_cap_stock_div_stock_high_stock_low_stock_pe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='cap',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='div',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='high',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='low',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='pe',
        ),
    ]
