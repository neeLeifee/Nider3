from django.db import models
from django.contrib.auth.models import User
from hobbies.models import Hobby


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    hobbies = models.ManyToManyField(Hobby, verbose_name='Увлечения')
    city = models.CharField('Город', max_length=64)
    gender = models.CharField('Пол', max_length=100)

    def __str__(self):  # чтобы в БД показывалось название экземпляра
        return self.user.username
