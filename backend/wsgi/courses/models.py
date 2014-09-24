from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title   = models.CharField(max_length=100)
    desc    = models.CharField(max_length=500)
    points_reward  = models.PositiveIntegerField()

class Course(models.Model):
    name    = models.CharField(max_length=80)
    desc    = models.CharField(max_length=200)
    registrations = models.ManyToManyField(User, through="Registration")
    tasks = models.ManyToManyField(Task)

    registration_start  = models.DateTimeField()
    registration_end    = models.DateTimeField()

    registration_limit  = models.PositiveIntegerField() 

    def __str__(self):
        return self.name


class Registration(models.Model):
    user = models.ForeignKey(User)
    course = models.ForeignKey(Course)
    granted = models.BooleanField()
    code_master = models.BooleanField()

def get_registered_kids():
    courses = Course.objects.all()
    for course in courses:
        course.taken = Registration.objects.filter(course=course,code_master=False).count()
    return courses

def all_clean():
    return Course.objects.all()

class Ranking(models.Model):
    name = models.CharField(max_length=30)
    required_score = models.PositiveIntegerField()
    icon = models.ImageField(upload_to='rank_icons')

def get_start_rank():
    if Ranking.objects.all().exists():
        rank = Ranking.objects.order_by('-required_score').first()
        return rank
    else:
        rank = Ranking(name="Apprentice", required_score=0)
        rank.save()
        return rank

class ScoreProfile(models.Model):
    user = models.OneToOneField(User)
    current_rank = models.ForeignKey(Ranking)
    score   = models.PositiveIntegerField()

def get_score_profile(user):
    if ScoreProfile.objects.filter(user=user).exists():
        return ScoreProfile.objects.filter(user=user).first()
    else:
        profile = ScoreProfile(user=user, current_rank=get_start_rank(), score=0)
        profile.save()
        return profile

class CompilerProfile(models.Model):
    compile_cmd = models.CharField(max_length=100)
    execute_cmd = models.CharField(max_length=100)

class TaskSubmission(models.Model):
    task = models.ForeignKey(Task)
    valid = models.BooleanField()
    content_file = models.FileField(upload_to='submissions/')     
    submitted_by = models.ForeignKey(User)

    def execute(self, input=""):
        pass  

class TestCase(models.Model):
    task = models.ForeignKey(Task)

    def is_valid(self, submission):
        return False

'''
class SimpleTestCase(TestCase):
    input_file = models.FileField()
    output_file= models.FileField()

    def is_valid(self,submission):
        input   = "" #TODO read input file content
        output  = "" #TODO read output file content
        test_out= submission.execute(input)

        return output==test_out

class CustomValidatorTestCase(TestCase):
    pass
'''




