# Generated by Django 3.1.3 on 2020-11-25 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_auto_20201124_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='restaurantLogo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
