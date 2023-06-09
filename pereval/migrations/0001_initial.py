# Generated by Django 4.2 on 2023-04-13 10:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(blank=True, default=0.0, null=True, verbose_name='Широта')),
                ('longitude', models.FloatField(blank=True, default=0.0, null=True, verbose_name='Долгота')),
                ('height', models.IntegerField(blank=True, default=0, null=True, verbose_name='Высота над уровнем моря, м')),
            ],
            options={
                'verbose_name': 'Координаты',
                'verbose_name_plural': 'Координаты',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.ImageField(null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Изображение')),
                ('title', models.CharField(max_length=255)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Изображения',
                'verbose_name_plural': 'Изображения',
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winter', models.CharField(blank=True, choices=[('н/к', 'некатегорийный'), ('1А', '1А'), ('1Б', '1Б'), ('2А', '2А'), ('2А', '2Б'), ('3А', '3А'), ('3Б', '3Б')], max_length=15, verbose_name='Зима')),
                ('summer', models.CharField(blank=True, choices=[('н/к', 'некатегорийный'), ('1А', '1А'), ('1Б', '1Б'), ('2А', '2А'), ('2А', '2Б'), ('3А', '3А'), ('3Б', '3Б')], max_length=15, verbose_name='Лето')),
                ('autumn', models.CharField(blank=True, choices=[('н/к', 'некатегорийный'), ('1А', '1А'), ('1Б', '1Б'), ('2А', '2А'), ('2А', '2Б'), ('3А', '3А'), ('3Б', '3Б')], max_length=15, verbose_name='Осень')),
                ('spring', models.CharField(blank=True, choices=[('н/к', 'некатегорийный'), ('1А', '1А'), ('1Б', '1Б'), ('2А', '2А'), ('2А', '2Б'), ('3А', '3А'), ('3Б', '3Б')], max_length=15, verbose_name='Весна')),
            ],
            options={
                'verbose_name': 'Уровень сложности',
                'verbose_name_plural': 'Уровень сложности',
            },
        ),
        migrations.CreateModel(
            name='PerevalAdded',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beauty_title', models.CharField(max_length=255, verbose_name='Тип')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('other_titles', models.CharField(blank=True, max_length=255, verbose_name='Другие названия')),
                ('connect', models.CharField(blank=True, max_length=255, verbose_name='Что соединяет')),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('new', 'новый'), ('pending', 'модератор взял в работу'), ('accepted', 'модерация прошла успешно'), ('rejected', 'модерация прошла, информация не принята')], default='new', max_length=10)),
                ('coords', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pereval.coords', verbose_name='Координаты')),
            ],
            options={
                'verbose_name': 'Перевал',
                'verbose_name_plural': 'Перевал',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(blank=True, max_length=14, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed.", regex='^\\+?1?\\d{9,12}$')])),
                ('fam', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('otc', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Пользователи',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='PerevaladdedImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pereval.images')),
                ('perevaladded', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pereval.perevaladded')),
            ],
            options={
                'verbose_name': 'Перевал-Изображение',
                'verbose_name_plural': 'Перевал-Изображение',
            },
        ),
        migrations.AddField(
            model_name='perevaladded',
            name='images',
            field=models.ManyToManyField(through='pereval.PerevaladdedImages', to='pereval.images'),
        ),
        migrations.AddField(
            model_name='perevaladded',
            name='level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pereval.level', verbose_name='Категория трудности'),
        ),
        migrations.AddField(
            model_name='perevaladded',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pereval.users', verbose_name='Ползователь'),
        ),
    ]
