from django.db import models


# Create your models here.
class Table(models.Model):
    title = models.CharField(max_length=30, verbose_name='Заголовок')
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    quantity = models.IntegerField(default=0, verbose_name='Количество')
    distance = models.IntegerField(verbose_name='Расстояние')
