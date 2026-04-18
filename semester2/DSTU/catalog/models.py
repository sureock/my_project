from django.db import models
from .validators import real_age, real_number, real_email


class Teacher(models.Model):
    first_name = models.CharField(
        max_length=100,
        blank=False,
    )
    last_name = models.CharField(
        max_length=100,
        blank=False
    )
    patronymic = models.CharField(
        max_length=100,
        blank=True
    )


class TeacherInfo(models.Model):
    teacher = models.OneToOneField(
        Teacher,
        on_delete=models.CASCADE,
        related_name='info',
        primary_key=True
    )
    phone = models.CharField(
        max_length=30,
        blank=False,
        unique=True,
        validators=[real_number]
    )
    bio = models.TextField(
        blank=True
    )
    email = models.TextField(
        blank=True,
        unique=True,
        validators=[real_email]
    )
    birthday = models.DateField( 
        validators=[real_age],
    )


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
