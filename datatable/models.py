from django.db import models

# Create your models here.
class employee(models.Model):
    name = models.CharField(max_length=20)
    position = models.CharField(max_length=20)
    office = models.CharField(max_length=20)
    age = models.IntegerField(max_length=10)
    date = models.DateField()
    salary = models.IntegerField()

