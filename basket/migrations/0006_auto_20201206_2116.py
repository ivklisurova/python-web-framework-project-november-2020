# Generated by Django 3.1.3 on 2020-12-06 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0005_auto_20201206_1903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productlineitems',
            name='basket_id',
        ),
        migrations.RemoveField(
            model_name='productlineitems',
            name='product_ptr',
        ),
        migrations.DeleteModel(
            name='Basket',
        ),
        migrations.DeleteModel(
            name='ProductLineItems',
        ),
    ]
