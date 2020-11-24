# Generated by Django 3.1.3 on 2020-11-21 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='phone_num',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.CreateModel(
            name='LevelTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('templatename', models.CharField(blank=True, max_length=200)),
                ('timetoCook', models.CharField(blank=True, max_length=200)),
                ('bestseller', models.BooleanField(default=False)),
                ('recommended', models.BooleanField(default=False)),
                ('social1', models.URLField()),
                ('social2', models.URLField()),
                ('resid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='LevelOne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dishtype', models.CharField(blank=True, max_length=200)),
                ('dishname', models.CharField(blank=True, max_length=200)),
                ('cuisine', models.CharField(blank=True, max_length=200)),
                ('veg', models.BooleanField(null=True)),
                ('dishpic', models.ImageField(null=True, upload_to='')),
                ('resid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.restaurant')),
            ],
        ),
    ]
