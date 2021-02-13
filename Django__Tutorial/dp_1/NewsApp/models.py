from django.db import models
from django.utils import timezone

class News(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    description = models.TextField()
    pub_date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.author

class SportNews(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.author

class RegistrationData(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Customers(models.Model):
    CustomerID = models.IntegerField()
    CustomerName=models.CharField(max_length=70)
    ContactName = models.CharField(max_length=70)
    Address=models.EmailField(max_length=70)
    City=models.CharField(max_length=70)
    PostalCode = models.CharField(max_length=70)
    Country = models.CharField(max_length=70)

