from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class HeaderHome(models.Model):
    '''Модель для редактирования жедера страницы'''
    greeting = models.CharField(max_length=30, verbose_name='Приветствие', blank=False)
    position = models.CharField(max_length=30, verbose_name='Должность', blank=False)
    
    class Meta:
        verbose_name = 'Параметры заголовка'
        verbose_name_plural = 'Параметры заголовка'
        ordering = ['-id']

class ContensBar(models.Model):
    '''  Модель для редоктирования области с  progressbar'''
    name = models.CharField(max_length=200, verbose_name='Заголовок', blank=False)
    content = models.TextField(verbose_name='Описание', blank=False)
    barOneText = models.CharField(max_length=20, verbose_name='Название верхнего progressbar', blank=False)
    barOneProcent = models.IntegerField(default=0, blank=False, verbose_name='Процент заполнения верхнего progressbar', validators=[MinValueValidator(0), MaxValueValidator(100)])
    barTwoText = models.CharField(max_length=20, verbose_name='Название центрального progressbar', blank=False)
    barTwoProcent = models.IntegerField(default=0, blank=False, verbose_name='Процент заполнения центрального progressbar', validators=[MinValueValidator(0), MaxValueValidator(100)])
    barFhreeText = models.CharField(max_length=20, verbose_name='Название нижнего progressbar', blank=False)
    barFhreeProcent = models.IntegerField(default=0, blank=False, verbose_name='Процент нижнего progressbar', validators=[MinValueValidator(0), MaxValueValidator(100)])
    buttonName = models.CharField(max_length=20, verbose_name='Название кнопки', blank=False)
    buttonLink = models.URLField(verbose_name='Ссылка кнопки')
    class Meta:
        verbose_name = 'Область progressbar'
        verbose_name_plural = 'Область progressbar'
        ordering = ['-id']

class ContentServices(models.Model):
    ''' Таблица для области My Services  '''
    nameOne = models.CharField(max_length=21, verbose_name='Заголовок левого блока', blank=False)
    contentOne = models.CharField(max_length=100, verbose_name='Описание левого блока', blank=False)
    nameTwo = models.CharField(max_length=21, verbose_name='Заголовок центрального блока', blank=False)
    contentTwo = models.CharField(max_length=100, verbose_name='Описание центрального блока', blank=False)
    nameThree = models.CharField(max_length=21, verbose_name='Заголовок правого блока', blank=False)
    contentThree = models.CharField(max_length=100, verbose_name='Описание правого блока', blank=False)
    class Meta:
        verbose_name = 'Область мои сервисы'
        verbose_name_plural = 'Область мои сервисы'
        ordering = ['-id']

class ContentWorks(models.Model):
    ''' Таблица всех работ  '''
    name = models.CharField(max_length=30, verbose_name='Название работы', blank=False)
    theme = models.CharField(max_length=20, verbose_name='Рубрика', blank=False)
    content = models.TextField(verbose_name='Описание работы', blank=False)
    preview = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Изоброжение новости', blank=True)
    buttonName = models.CharField(max_length=20, verbose_name='Название кнопки', blank=False)
    buttonLink = models.URLField(verbose_name='Ссылка кнопки')
    datePublication = models.DateTimeField(verbose_name='Дата публикации', default=timezone.now)
    dateCreate = models.DateTimeField(auto_now=True, verbose_name='Дата создания/обновления')
    publication = models.BooleanField(default=False, blank=False, verbose_name='Опубликовано')

    def get_absolute_url(self):
        return reverse('view_work', kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Мои работы'
        verbose_name_plural = 'Мои работы'
        ordering = ['-dateCreate']

class SettingSidebar(models.Model):
    ''' Залоговок сайдбара  '''
    name = models.CharField(max_length=30, verbose_name='Залоговок сайдбара', blank=False)

    class Meta:
        verbose_name = 'Залоговок сайдбара'
        verbose_name_plural = 'Залоговок сайдбара'
        ordering = ['-id']


class ContentSlidebar(models.Model):
    ''' Таблица для сайдбара Каждая строка - это один слайд  '''
    header = models.CharField(max_length=20, verbose_name='Залоговок слайда', blank=False)
    content = models.TextField(verbose_name='Описание слайда', blank=False)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото на слайде', blank=True)
    name = models.CharField(max_length=30, verbose_name='Имя', blank=True)
    position = models.CharField(max_length=30, verbose_name='Должность', blank=True)
    dateCreate = models.DateTimeField(auto_now=True, verbose_name='Дата создания/обновления')
    publication = models.BooleanField(default=False, blank=False, verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Слайды'
        verbose_name_plural = 'Слайды'
        ordering = ['-id']

class ContentFooter(models.Model):
    ''' Таблица для footer
    incLinkThree - это имя класса. Имена классов можно взять отсюда: https://fontawesome.com/v4.7.0/icons/#brand
      '''
    nameOne = models.CharField(max_length=20, verbose_name='Залоговок 1', blank=False)
    nameTwo = models.CharField(max_length=20, verbose_name='Залоговок 2', blank=False)
    content = models.TextField(verbose_name='Описание', blank=False)

    nameLinkOne = models.CharField(max_length=15, verbose_name='Заголовок кнопки 1', blank=False)
    incLinkOne = models.CharField(max_length=20, verbose_name='Класс иконки кнопки 1')
    LinkOne = models.URLField(verbose_name='Ссылка кнопки 1')

    nameLinkTwo = models.CharField(max_length=15, verbose_name='Заголовок кнопки 2', blank=False)
    incLinkTwo = models.CharField(max_length=20, verbose_name='Класс иконки кнопки 2')
    LinkTwo = models.URLField(verbose_name='Ссылка кнопки 2')

    nameLinkThree = models.CharField(max_length=15, verbose_name='Заголовок кнопки 3', blank=False)
    incLinkThree = models.CharField(max_length=20, verbose_name='Класс иконки кнопки 3')
    LinkThree = models.URLField(verbose_name='Ссылка кнопки 3')

    nameLinkFour = models.CharField(max_length=15, verbose_name='Заголовок кнопки 4', blank=False)
    incLinkFour = models.CharField(max_length=20, verbose_name='Класс иконки кнопки 4')
    LinkFour = models.URLField(verbose_name='Ссылка кнопки 4')

    class Meta:
        verbose_name = 'Footer'
        verbose_name_plural = 'Footer'
        ordering = ['-id']