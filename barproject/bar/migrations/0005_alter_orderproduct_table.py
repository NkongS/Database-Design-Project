# Generated by Django 5.0.3 on 2024-03-30 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0004_alter_orderproduct_table_alter_orders_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='orderproduct',
            table='orderproduct',
        ),
    ]