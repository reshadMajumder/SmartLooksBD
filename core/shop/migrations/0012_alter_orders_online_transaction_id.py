# Generated by Django 5.0.3 on 2024-04-01 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_alter_orders_options_alter_products_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='online_transaction_id',
            field=models.CharField(default='N/A', max_length=20),
        ),
    ]
