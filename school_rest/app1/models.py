from django.db import models

# Create your models here.
class students(models.Model):
    student_id=models.IntegerField(unique=True)
    student_name=models.CharField(max_length=20)
    student_age=models.IntegerField()
