from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name    = models.CharField(max_length=80)
    desc    = models.CharField(max_length=200)
    registrations = models.ManyToManyField(User, through="Registration")

    registration_start  = models.DateTimeField()
    registration_end    = models.DateTimeField()

    registration_limit  = models.PositiveIntegerField() 


class Registration(models.Model):
    user = models.ForeignKey(User)
    course = models.ForeignKey(Course)
    granted = models.BooleanField()
    code_master = models.BooleanField()

def all():
    courses = Course.objects.all()
    for course in courses:
        course.taken = course.registrations.count()
    return courses

def all_clean():
    return Course.objects.all()

