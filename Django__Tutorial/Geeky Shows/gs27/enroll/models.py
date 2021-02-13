from django.db import models

class Student(models.Model):
    stuid = models.ImageField()
    stuname=models.CharField(max_length=70)
    stuemail=models.EmailField(max_length=70)
    stupss=models.CharField(max_length=70)





