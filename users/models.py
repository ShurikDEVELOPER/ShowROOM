from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    phone = PhoneNumberField(null=False, blank=True, unique=True)
    city = models.CharField(max_length=30, blank=True)
    avatar = models.ImageField('Аватар', upload_to='media/', null=True, blank=True)

    REQUIRED_FIELDS = ['email', 'city', 'avatar', ]

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'