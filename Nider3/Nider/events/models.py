from django.db import models
from hobbies.models import Hobby
from users.models import Profile


class Event(models.Model):
    """Модель события"""
    name = models.CharField('Название', max_length=128)
    description = models.CharField('Описание', max_length=2048)
    address = models.CharField('Адрес', max_length=2048)
    date = models.CharField('Дата', max_length=100)
    hobby = models.ForeignKey(Hobby, verbose_name='Тема', on_delete=models.CASCADE)
    participants = models.ManyToManyField(Profile, verbose_name='Участники')
    creator_name = models.CharField('Создатель', max_length=128)  # Char, т.к. нельзя привязывать одну и ту же модель

    def __str__(self):  # чтобы в БД показывалось название экземпляра
        return self.name
