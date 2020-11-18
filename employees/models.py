from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    employee_id = models.CharField(max_length=3, default=0)

    def __str__(self):
        return f"{self.name} | {self.employee_id} | {self.department} | {self.position}"
