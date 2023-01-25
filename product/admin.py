from django.contrib import admin, messages
from django.conf.locale import sq
from django.db.models import QuerySet

from core.enams.product_enams import Currency
from product.models import Category, Product, Raiting


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]
    ordering = ['name']
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'description', 'price', 'stock']
    ordering = ['name']
    search_fields = ['category', 'name', 'price']

    @admin.action(description='Изменить валюту элементов на доллары США')
    def change_to_usd(self, request, qs: QuerySet):
        update_product = qs.update(currency = Currency.USD)
        self.message_user(
            request,
            f'Обновлено {update_product} записей',
            messages.SUCCESS
        )

@admin.register(Raiting)
class RaitingAdmin(admin.ModelAdmin):
    list_display = ['value', 'product']
    ordering = ['value']
    search_fields = ['value']

    @admin.action(description='Изменить рейтинг у всех объектов на 10')
    def change_to_10(self, request, qs: QuerySet):
        update_value = qs.update(value=10)
        self.message_user(
            request,
            f'Обновлено {update_value} записей',
            messages.SUCCESS
        )


