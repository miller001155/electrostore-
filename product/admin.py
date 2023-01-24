from django.contrib import admin

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

@admin.register(Raiting)
class RaitingAdmin(admin.ModelAdmin):
    list_display = ['value', 'product']
    ordering = ['value']
    search_fields = ['value']

