from django.db import models

# Create your models here.

class Contact(models.Model):
    
    name = models.CharField(max_length=124)
    email = models.CharField(max_length=124)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=32)
    message = models.TextField()