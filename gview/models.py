from django.db import models

# Create your models here.

from django.db import models

class Breed(models.Model):
    name = models.CharField(max_length=200)

class Cat(models.Model):
    nickname = models.CharField(max_length=200, default='Silvester')
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE, null=False, default=1)
    weight = models.FloatField(default=10)

class Dog(models.Model):
    name = models.CharField(max_length=128)

class Horse(models.Model):
    name = models.CharField(max_length=128)

class Car(models.Model):
    name = models.CharField(max_length=128)

