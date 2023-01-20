from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class NEWS(models.Model):
    news_title = models.CharField(max_length=80)
    news_desc = HTMLField()