from django.core.exceptions import ValidationError

def check_age(age):
    if age < 18:
        raise ValidationError("Вы должны быть совершеннолетним")

def check_phone(phone):
    if len(phone) != 13 or phone[0] != '+':
        raise ValidationError('Проверьте правильность ввода номера')
