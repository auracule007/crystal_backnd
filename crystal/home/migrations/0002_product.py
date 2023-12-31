# Generated by Django 4.2.6 on 2023-10-21 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(default='')),
                ('stockImg', models.ImageField(default='product.jpg', upload_to='Product')),
                ('stockPrice', models.IntegerField()),
                ('discountedPrice', models.FloatField(blank=True, null=True)),
                ('stockQuantity', models.IntegerField()),
                ('maxQuantity', models.IntegerField(blank=True, null=True)),
                ('minQuantity', models.IntegerField(blank=True, null=True)),
                ('shortDescription', models.TextField(blank=True, null=True)),
                ('longDescription', models.TextField(blank=True, null=True)),
                ('uploaded', models.DateField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
    ]
