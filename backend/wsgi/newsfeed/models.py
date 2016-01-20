from django.contrib.auth.models import User
from django.db import models


class NewsItem(models.Model):
    title = models.TextField()
    hide = models.BooleanField(default=False)
    body = models.TextField()
    author = models.ForeignKey(User)
    time_stamp = models.DateTimeField(auto_now_add=True)
