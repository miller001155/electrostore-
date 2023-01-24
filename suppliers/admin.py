from django.contrib import admin

from suppliers.models import Supplier


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'product', 'reviews']
    ordering = ['name']
    search_fields = ['name', 'location']
