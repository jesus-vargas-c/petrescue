from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=70)
    age = models.IntegerField()
    phone = models.CharField(max_length=12)
    email= models.EmailField()
    address = models.TextField()

    def __str__(self):
        return '{} {}'.format(self.name, self.last_name)