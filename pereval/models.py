from django.contrib.auth.models import User
from django.db import models


class PerevalAdded(models.Model):
    NEW = 'new'
    PENDING = 'pending'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'
    STATUS_CHOICES = [
    ("new", "новый"),
    ("pending",  "модератор взял в работу"),
    ("accepted", "модерация прошла успешно"),
    ("rejected",  "модерация прошла, информация не принята"),
    ]

    beauty_title = models.CharField(max_length=255, verbose_name='Тип')
    title = models.CharField(max_length=255, verbose_name='Название')
    other_titles = models.CharField(max_length=255, blank=True, verbose_name='Другие названия')
    connect = models.CharField(max_length=255, blank=True)
    add_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coords = models.ForeignKey('Coords', on_delete=models.CASCADE)
    level = models.ForeignKey('Level', on_delete=models.CASCADE, verbose_name='Категория трудности')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=NEW)
    # images =

    def __str__(self):
        return self.title


class Users(models.Model):
    email = models.EmailField(unique=True)
    fam = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    otc = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.name}'


class Level(models.Model):
    LEVEL_CHOICES = [
    ("н/к", "некатегорийный"),
    ("1А", "1А"),
    ("1Б", "1Б"),
    ("2А",  "2А"),
    ("2А", "2Б"),
    ("3А",  "3А"),
    ("3Б", "3Б"),
    ]

    winter = models.CharField(max_length=15, choices=LEVEL_CHOICES, verbose_name='Зима', blank=True, null=True)
    summer = models.CharField(max_length=15, choices=LEVEL_CHOICES, verbose_name='Лето', blank=True, null=True)
    autumn = models.CharField(max_length=15, choices=LEVEL_CHOICES, verbose_name='Осень', blank=True, null=True)
    spring = models.CharField(max_length=15, choices=LEVEL_CHOICES, verbose_name='Весна', blank=True, null=True)

    def __str__(self):
        return f'летом: {self.summer}'


class Coords(models.Model):
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    height = models.IntegerField(verbose_name='Высота над уровнем моря')

    def __str__(self):
        return f'GPS: {self.latitude}, {self.longitude} Высота: {self.height}'


# class Images(models.Model):
#     pereval = models.ForeignKey('PerevalAdded', on_delete=models.CASCADE, related_name='images')
#     data = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Изображение', null=True)
#     title = models.CharField(max_length=255)
#     date_added = models.DateField(auto_now_add=True)
