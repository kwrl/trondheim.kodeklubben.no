from django.db import models
from tinymce.models import HTMLField

class NewsItem(models.Model):
    title   = models.CharField(max_length=80)
    intro   = models.CharField(max_length=200)
    body    = HTMLField() 
    time_stamp = models.DateTimeField(auto_now_add=True)
