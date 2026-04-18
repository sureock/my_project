from django.contrib.auth.models import AbstractUser
from django.db import models
from .validators import real_email, real_number


class MyUser(AbstractUser):
    bio = models.TextField(
        'Биография',
        blank=True,
        null=True,
    )
    email = models.TextField(
        'Почта',
        unique=True,
        validators=[real_email]
    )
    phone = models.CharField(
        'Телефон',
        max_length=30,
        blank=False,
        unique=True,
        validators=[real_number]
    )
