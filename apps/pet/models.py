from django.db import models
from apps.adoption.models import Person

# Create your models here.

class Vaccine(models.Model):
    name = models.CharField(max_length=25)
    expiration_date = models.DateField()


class Pet(models.Model):
    name = models.CharField(max_length=50)
    sexpet = models.CharField(max_length=10)
    age = models.IntegerField()
    rescue_date = models.DateField()
    person = models.ForeignKey(Person, null=True, blank=True, on_delete=models.CASCADE)
    vaccine = models.ManyToManyField(Vaccine, blank=True)



