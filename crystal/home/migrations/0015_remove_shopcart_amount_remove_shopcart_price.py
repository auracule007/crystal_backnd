# Generated by Django 4.2.6 on 2023-10-29 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_shopcart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopcart',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='shopcart',
            name='price',
        ),
    ]
