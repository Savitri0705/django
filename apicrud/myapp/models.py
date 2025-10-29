from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=80)
    age=models.IntegerField()
    marks=models.FloatField()
    emailid=models.EmailField()

    def __str__(self):
        return self.name