from django.db import models

class StockOfProduct(models.TextChoices):
    Storage = 'Storage', 'Storage' # на складе
    NotAvalible = 'NotAvalible', 'NotAvalible' # нет в наличии
    Basket = 'Basket', 'Basket' # в корзине

class Currency(models.TextChoices):
    EUR = 'EUR', 'EUR'
    USD =  'USD', 'USD'
    RUB = 'RUB', 'RUB'
    BEL = 'BEL', 'BEL'