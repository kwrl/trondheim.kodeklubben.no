from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name    = models.CharField(max_length=80)
    desc    = models.CharField(max_length=200)

    registration_start  = models.DateTimeField()
    registration_end    = models.DateTimeField()

    registration_limit  = models.PositiveIntegerField() 


class Registration(models.Model):
    user    = models.ForeignKey(User)
    course  = models.ForeignKey(Course)

    granted = models.BooleanField()
