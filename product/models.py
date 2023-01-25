from django.db import models

from core.abstract_models import AbstractDefaultModel
from core.enams.product_enams import StockOfProduct, Currency
from core.validators import check_raiting


class Category(AbstractDefaultModel):
    name = models.CharField(max_length=255, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name

class Product(AbstractDefaultModel):
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=255, db_index=True)
    image = models.ImageField(
        upload_to='products/%Y/%m/%d',
        blank=True,
        verbose_name='Изображение'
    )
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        verbose_name='Цена',
        default=20,
    )
    currency = models.CharField(
        max_length=4,
        choices= Currency.choices,
        default= Currency.BEL,
        verbose_name='Валюта'
    )
    stock = models.CharField(
        max_length=12,
        choices=StockOfProduct.choices,
        default=StockOfProduct.Storage,
        verbose_name='Наличие'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

class Raiting(AbstractDefaultModel):
    value = models.IntegerField(validators=[check_raiting], default=1)
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name='raiting',
        verbose_name='Рейтинг',
    )

    class Meta:
        ordering = ('value',)
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'