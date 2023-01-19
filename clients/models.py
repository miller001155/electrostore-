from django.db import models
from django_countries.fields import CountryField

from electrostore.core.abstract_models import AbstractDefaultModel
from electrostore.core.validators import check_age, check_phone


class Client(AbstractDefaultModel):
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    second_name = models.CharField(max_length=255, verbose_name='Фамилия')
    age = models.IntegerField(verbose_name='Возраст',
                              validators=[check_age])
    email = models.EmailField(verbose_name='Почта')
    phone = models.CharField(max_length=13,
                             verbose_name='Телефон',
                             validators=[check_phone])
    location = CountryField(verbose_name='Страна')

    def __str__(self):
        return self.first_name
    class Meta:
        ordering = ('first_name',)
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'

class Balance(AbstractDefaultModel):
    value = models.DecimalField(max_digits=7,
                                decimal_places=2,
                                verbose_name='Количество денег')
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        verbose_name='покупатель',
    )

    class Meta:
        ordering = ('value',)
        verbose_name = 'Баланс'
        verbose_name_plural = 'Балансы'
