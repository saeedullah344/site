from django.db import models

class service(models.Model):
    name = models.CharField(max_length=80)
    fname = models.CharField(max_length=80)
    mesage = models.TextField()

# Create your models here.
