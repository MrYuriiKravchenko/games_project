from django.contrib.auth.models import User
from django.db import models


class Games(models.Model):
    RATING_CHOICES = (
        (1, 'Мусор'),
        (2, 'Проходняк'),
        (3, 'Можно поиграть'),
        (4, 'Похвально'),
        (5, 'Изумительно')
    )
    time_create = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    number_of_players = models.IntegerField(null=True, blank=True)
    controller = models.BooleanField(default=False)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, null=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Игры'
        verbose_name_plural = 'Игры'


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'