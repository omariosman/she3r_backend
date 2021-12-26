from django.db import models
from django.db.models.base import Model

# Create your models here.

class Verse(models.Model):
    part_one = models.CharField(max_length=100)
    part_two = models.CharField(max_length=100)
    poet = models.CharField(max_length=50)


    def __str__(self):
        return self.part_one

