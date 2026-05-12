from django.db import models
from .validators import real_age, real_number, real_email
from users.models import Teacher


class Course(models.Model):
    teacher = models.ForeignKey(
        Teacher,
        null=True,
        on_delete=models.SET_NULL,
        related_name="course"
    )
    title = models.CharField(
        max_length=100,
        null=False
    )
    date = models.DateField(
        blank=True
    )


class Student(models.Model):
    courses = models.ManyToManyField(
        Course
    )
    first_name = models.CharField(
        max_length=100,
        null=False
    )
    last_name = models.CharField(
        max_length=100,
        null=False
    )
    patronymic = models.CharField(
        max_length=100,
        null=True
    )
    email = models.TextField(
        blank=False,
        unique=True,
        default='no email',
        validators=[real_email]
    )
    phone = models.CharField(
        max_length=30,
        blank=False,
        unique=True,
        validators=[real_number]
    )
    birthday = models.DateField(
        null=True,
        blank=True,
        validators=[real_age]
    )
