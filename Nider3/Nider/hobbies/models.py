from django.db import models


class HobbyCategory(models.Model):
    """Модель категории увлечения"""
    name = models.CharField('Название', max_length=128)

    def __str__(self):  # чтобы в БД показывалось название экземпляра
        return self.name


class Hobby(models.Model):
    """Модель увлечения"""
    name = models.CharField('Название', max_length=128)
    description = models.CharField('Описание', max_length=2048)
    category = models.ForeignKey(HobbyCategory, verbose_name='Категория', on_delete=models.CASCADE)

    def __str__(self):  # чтобы в БД показывалось название экземпляра
        return self.name
