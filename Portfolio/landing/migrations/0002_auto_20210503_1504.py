# Generated by Django 3.2 on 2021-05-03 12:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contensbar',
            name='barFhreeProcent',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Процент нижнего progressbar'),
        ),
        migrations.AlterField(
            model_name='contensbar',
            name='barOneProcent',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Процент заполнения верхнего progressbar'),
        ),
        migrations.AlterField(
            model_name='contensbar',
            name='barTwoProcent',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Процент заполнения центрального progressbar'),
        ),
    ]
