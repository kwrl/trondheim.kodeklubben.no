from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ExtraCourseManager(models.Manager):
    def open_registration(self):
        all_courses = self.all()
        return all_courses.filter(registration_start__lt=timezone.now(),
                                  registration_end__gt=timezone.now())

class Course(models.Model):
    name = models.CharField(max_length=80)
    desc = models.CharField(max_length=200)
    registrations = models.ManyToManyField(User,
                                           through="Registration")

    registration_start = models.DateField()
    registration_end = models.DateField()

    registration_limit = models.PositiveIntegerField()
    objects = ExtraCourseManager()

    def __str__(self):
        return self.name


class Registration(models.Model):
    KID = 0
    CODE_MASTER = 1
    RESERVE = 2
    ROLES = (
        (KID, 'Kursdeltager'),
        (CODE_MASTER, 'Veileder'),
        (RESERVE, 'Reserveveileder')
    )
    user = models.ForeignKey(User)
    course = models.ForeignKey(Course)
    granted = models.BooleanField(default=False)
    code_master = models.BooleanField(default=False)
    role = models.PositiveIntegerField(choices=ROLES, default=KID)

    class Meta:
        unique_together=(('user','course'))
