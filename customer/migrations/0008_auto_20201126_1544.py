# Generated by Django 3.1.3 on 2020-11-26 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_restaurant_restaurantlogo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='restaurantImage',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='restaurantLogo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]