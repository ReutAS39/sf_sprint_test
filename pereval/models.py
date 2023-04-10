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

    beauty_title = models.CharField(max_length=255, verbose_name='')
    title = models.CharField(max_length=255, verbose_name='Название')
    other_titles = models.CharField(max_length=255, verbose_name='')
    connect = models.CharField(max_length=255, null=True)
    add_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coords = models.ForeignKey('Coords', on_delete=models.CASCADE)
    level = models.ForeignKey('Level', on_delete=models.CASCADE, verbose_name='Категория трудности')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=NEW)
    #images =


LEVEL_CHOICES = [
    ("н/к", "некатегорийный"),
    ("1А", "новый"),
    ("2А",  "модератор взял в работу"),
    ("2А", "модерация прошла успешно"),
    ("3А",  "модерация прошла, информация не принята"),
    ("3Б", "модерация прошла, информация не принята"),
    ]


class Level(models.Model):
    winter = models.CharField(max_length=15, choices=LEVEL_CHOICES, verbose_name='Зима', null=True)
    summer = models.CharField(max_length=15, choices=LEVEL_CHOICES, verbose_name='Лето', null=True)
    autumn = models.CharField(max_length=15, choices=LEVEL_CHOICES, verbose_name='Осень', null=True)
    spring = models.CharField(max_length=15, choices=LEVEL_CHOICES, verbose_name='Весна', null=True)


class Coords(models.Model):
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    height = models.IntegerField(verbose_name='Высота над уровнем моря')


class Images(models.Model):
    pereval = models.ForeignKey('PerevalAdded', on_delete=models.CASCADE, related_name='images')
    data = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Изображение', null=True)
    title = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
