from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    college_id = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    college_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name} '
