from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=30)
    number=models.IntegerField(null=True)

    def __str__(self):
        return f"{self.number} - {self.name}"