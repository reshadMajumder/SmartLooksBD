# Generated by Django 4.1.7 on 2024-04-04 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_products_dummyprice_products_instock_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='thana',
        ),
    ]
