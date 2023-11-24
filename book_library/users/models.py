from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        blank=False,
        null=False,
        verbose_name='Имя пользователя',
    )
    email = models.EmailField(
        max_length=150,
        unique=True,
        blank=False,
        null=False,
        verbose_name='Электронная почта'
    )
    date_joined = models.DateTimeField(
        default=timezone.now,
        verbose_name='Дата регистрации',
    )

    class Meta:
        ordering = ('username',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
