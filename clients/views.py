from django.http import HttpResponse


def home(reqvest):
    return HttpResponse('Домашняя страница')
