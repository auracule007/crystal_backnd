# Generated by Django 4.2.6 on 2023-10-29 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_shopcart_amount_shopcart_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopcart',
            name='amount',
            field=models.IntegerField(),
        ),
    ]
