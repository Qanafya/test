from django.db import models

# Create your models here.

class Workers(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    date_of_start = models.DateField(max_length=255)
    salary = models.IntegerField()
    working_for = models.ForeignKey('Managers', default=None, on_delete=models.SET_NULL, null=True)

class Managers(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    date_of_start = models.DateField(max_length=255)
    salary = models.IntegerField()
    working_for = models.ForeignKey('Directors', default=None, on_delete=models.SET_NULL, null=True)

class Directors(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    date_of_start = models.DateField(max_length=255)
    salary = models.IntegerField()

