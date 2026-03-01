from django.db import models


class Authors(models.Model):
    id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=15, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    courses = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'authors'


class Courses(models.Model):
    id = models.IntegerField(blank=True, null=True)
    number = models.CharField(max_length=15, blank=True, null=True)
    date = models.CharField(max_length=15, blank=True, null=True)
    name = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'courses'
