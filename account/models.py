from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 200)
    email = models.EmailField()

    def __str__(self):
        return self.username
class profile(models.Model):
    firstName = models.CharField(max_length = 200)
    lastName = models.CharField(max_length = 200)
    phoneNumber = models.CharField(max_length = 11)
    def __str__(self):
        return self.firstName
    
class address(models.Model):
    streetAddress = models.TextField()
    city = models.CharField(max_length = 200)
    zipCode = models.IntegerField()
    def __str__(self):
        return self.city