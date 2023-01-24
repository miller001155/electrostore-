# Generated by Django 4.1.3 on 2023-01-23 15:58

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now=True, null=True)),
                ('time_update', models.DateTimeField(auto_now=True, null=True)),
                ('is_published', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('location', django_countries.fields.CountryField(max_length=2, verbose_name='Страна')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('product', models.CharField(max_length=255, verbose_name='Товар')),
                ('reviews', models.TextField(max_length=500, verbose_name='Отзывы')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
                'ordering': ('name',),
            },
        ),
    ]