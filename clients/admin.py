from django.contrib import admin

from clients.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'second_name', 'age', 'email', 'phone', 'location']
    ordering = ['second_name']
    search_fields = ['second_name', 'email', 'phone']
    list_filter = ['first_name', 'second_name']

