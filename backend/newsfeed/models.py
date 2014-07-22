from django.db import models

class NewsItem(models.Model):
    title   = models.CharField(max_length=80)
    body    = models.CharField(max_length=400)
    time_stamp = models.DateTimeField(auto_now_add=True)
