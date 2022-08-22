import numbers
from tabnanny import verbose
from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField( max_length=50)
    last_name = models.CharField(max_length=33)
    number = models.IntegerField("numara")

    def __str__(self):
        return f"{self.number}-{self.first_name}"

    class Meta:
        ordering = ["-number"] # number'ın başına - konulduğu zaman tersten sıralar
        verbose_name_plural = ["öğrenciler"]