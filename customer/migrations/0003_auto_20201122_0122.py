# Generated by Django 3.1.3 on 2020-11-21 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20201122_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='duration',
            field=models.DurationField(null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='fifth',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='first',
            field=models.CharField(blank=True, default='', max_length=7),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='fourth',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='phone_num',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='plan',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='second',
            field=models.CharField(blank=True, default='', max_length=7),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='third',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='url',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
