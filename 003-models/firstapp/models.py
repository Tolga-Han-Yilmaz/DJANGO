from datetime import datetime
from django.db import models


# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    number=models.IntegerField()
    description=models.TextField(null=True,blank=True) # boş bırakılabilir
    register_date = models.DateField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)
    is_Active = models.BooleanField(default=True)

    def student_year_status(self):
        "Returns the student's year status."
        import datetime
        if self.register_date < datetime.date(2019,1,1):
            return "Senior"
        elif self.register_date < datetime.date(2020,1,1):
            return "Junior"
        else:
            return "Freshman"

    def __str__(self):
        return (f"{self.number} - {self.first_name}") # browserda tabloya eklenen kişileri gösterme şekli

    class Meta:
        ordering = ["number"] # browserda tablonun neye göre sıralama yapılacağını belirtir
        verbose_name_plural = "student_list" # browserda tablonun ismi değişti. (database'de değişmedi)