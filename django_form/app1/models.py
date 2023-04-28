from django.db import models

# Create your models here.
class Employee(models.Model):
    ename = models.CharField(max_length=500)
    eid = models.IntegerField()
    joining_date = models.DateField(auto_now=True)
    esalary = models.IntegerField()

    def __str__(self) -> str:
        return self.ename