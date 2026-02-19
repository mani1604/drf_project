from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    branch = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    
    