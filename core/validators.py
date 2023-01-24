from django.core.exceptions import ValidationError

def check_age(age):
    if age < 18:
        raise ValidationError("Вы должны быть совершеннолетним")

def check_phone(phone):
    if len(phone) != 13 or phone[0] != '+':
        raise ValidationError('Проверьте правильность ввода номера')

def check_raiting(value):
    if value > 10 or value < 1:
        raise ValidationError('Рейтинг выставляется от 1 до 10')