# Generated by Django 4.2 on 2023-04-25 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Detail', '0004_stock_div_yield_stock_high_stock_low_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='market_cap',
            new_name='cap',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='div_yield',
            new_name='div',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='pe_ratio',
            new_name='pe',
        ),
    ]