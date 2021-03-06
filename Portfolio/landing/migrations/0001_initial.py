# Generated by Django 3.2 on 2021-04-25 12:54

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContensBar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Описание')),
                ('barOneText', models.CharField(max_length=20, verbose_name='Название верхнего progressbar')),
                ('barOneProcent', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Процент заполнения верхнего progressbar')),
                ('barTwoText', models.CharField(max_length=20, verbose_name='Название центрального progressbar')),
                ('barTwoProcent', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Процент заполнения центрального progressbar')),
                ('barFhreeText', models.CharField(max_length=20, verbose_name='Название нижнего progressbar')),
                ('barFhreeProcent', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Процент нижнего progressbar')),
                ('buttonName', models.CharField(max_length=20, verbose_name='Название кнопки')),
                ('buttonLink', models.URLField(verbose_name='Ссылка кнопки')),
            ],
            options={
                'verbose_name': 'Область progressbar',
                'verbose_name_plural': 'Область progressbar',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ContentFooter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameOne', models.CharField(max_length=20, verbose_name='Залоговок 1')),
                ('nameTwo', models.CharField(max_length=20, verbose_name='Залоговок 2')),
                ('content', models.TextField(verbose_name='Описание')),
                ('nameLinkOne', models.CharField(max_length=15, verbose_name='Заголовок кнопки 1')),
                ('incLinkOne', models.URLField(verbose_name='Ссылка кнопки 1')),
                ('nameLinkTwo', models.CharField(max_length=15, verbose_name='Заголовок кнопки 2')),
                ('incLinkTwo', models.URLField(verbose_name='Ссылка кнопки 2')),
                ('nameLinkThree', models.CharField(max_length=15, verbose_name='Заголовок кнопки 3')),
                ('incLinkThree', models.URLField(verbose_name='Ссылка кнопки 3')),
                ('nameLinkFour', models.CharField(max_length=15, verbose_name='Заголовок кнопки 4')),
                ('incLinkFour', models.URLField(verbose_name='Ссылка кнопки 4')),
            ],
            options={
                'verbose_name': 'Footer',
                'verbose_name_plural': 'Footer',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ContentServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameOne', models.CharField(max_length=21, verbose_name='Заголовок правого блока')),
                ('contentOne', models.CharField(max_length=100, verbose_name='Описание правого блока')),
            ],
            options={
                'verbose_name': 'Область мои сервисы',
                'verbose_name_plural': 'Область мои сервисы',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ContentSlidebar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=20, verbose_name='Залоговок слайда')),
                ('content', models.TextField(verbose_name='Описание слайда')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото на слайде')),
                ('name', models.CharField(blank=True, max_length=30, verbose_name='Залоговок сайдбара')),
                ('position', models.CharField(blank=True, max_length=30, verbose_name='Залоговок сайдбара')),
                ('dateCreate', models.DateTimeField(auto_now=True, verbose_name='Дата создания/обновления')),
                ('publication', models.BooleanField(default=False, verbose_name='Опубликовано')),
            ],
            options={
                'verbose_name': 'Слайды',
                'verbose_name_plural': 'Слайды',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ContentWorks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название работы')),
                ('theme', models.CharField(max_length=20, verbose_name='Рубрика')),
                ('content', models.TextField(verbose_name='Описание работы')),
                ('preview', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Изоброжение новости')),
                ('buttonName', models.CharField(max_length=20, verbose_name='Название кнопки')),
                ('buttonLink', models.URLField(verbose_name='Ссылка кнопки')),
                ('datePublication', models.DateTimeField(default=datetime.date.today, verbose_name='Дата публикации')),
                ('dateCreate', models.DateTimeField(auto_now=True, verbose_name='Дата создания/обновления')),
                ('publication', models.BooleanField(default=False, verbose_name='Опубликовано')),
            ],
            options={
                'verbose_name': 'Мои работы',
                'verbose_name_plural': 'Мои работы',
                'ordering': ['-dateCreate'],
            },
        ),
        migrations.CreateModel(
            name='HeaderHome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('greeting', models.CharField(max_length=30, verbose_name='Приветствие')),
                ('position', models.CharField(max_length=30, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Параметры заголовка',
                'verbose_name_plural': 'Параметры заголовка',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='SettingSidebar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Залоговок сайдбара')),
            ],
            options={
                'verbose_name': 'Залоговок сайдбара',
                'verbose_name_plural': 'Залоговок сайдбара',
                'ordering': ['-id'],
            },
        ),
    ]
