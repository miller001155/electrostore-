from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE, verbose_name='Пользователь')
    bio=models.TextField(null=True, blank=True, verbose_name='Про себя')
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/" , verbose_name='Фото')
    facebook = models.CharField(max_length=50, null=True, blank=True)
    twitter = models.CharField(max_length=50, null=True, blank=True)
    instagram = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return str(self.user)
    class Meta:
        ordering = ('user',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
