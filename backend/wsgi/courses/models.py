from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Task(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    points_reward = models.PositiveIntegerField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Task, self).save()
        profiles = ScoreProfile.objects.all()
        for profile in profiles:
            profile.update()


class ExtraCourseManager(models.Manager):
    def open_registration(self):
        all_courses = self.all()
        return all_courses.filter(registration_start__lt=timezone.now(),
                                  registration_end__gt=timezone.now())

    def open_verbose(self):
        courses = self.open_registration()
        for course in courses:
            course.taken = \
                Registration.objects.filter(course=course,
                                            role=0).count()
        return courses


class Course(models.Model):
    name = models.CharField(max_length=80)
    desc = models.CharField(max_length=200)
    registrations = models.ManyToManyField(User,
                                           through="Registration")
    tasks = models.ManyToManyField(Task)

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
    granted = models.BooleanField()
    code_master = models.BooleanField()
    role = models.PositiveIntegerField(choices=ROLES, default=KID)


class Ranking(models.Model):
    name = models.CharField(max_length=30)
    required_score = models.PositiveIntegerField()
    icon = models.ImageField(upload_to='rank_icons')

    def save(self, *args, **kwargs):
        super(Ranking, self).save()
        profiles = ScoreProfile.objects.all()
        for profile in profiles:
            profile.update()


class ScoreProfile(models.Model):
    user = models.OneToOneField(User)
    current_rank = models.ForeignKey(Ranking)
    score = models.PositiveIntegerField()

    @classmethod
    def get_start_rank(cls):
        if Ranking.objects.all().exists():
            rank = Ranking.objects.order_by('required_score').first()
            return rank
        else:
            rank = Ranking(name="Apprentice", required_score=0)
            rank.save()
            return rank

    @classmethod
    def get_score_profile(cls, user):
        if ScoreProfile.objects.filter(user=user).exists():
            return ScoreProfile.objects.filter(user=user).first()
        else:
            profile = ScoreProfile(user=user,
                                   current_rank=ScoreProfile.get_start_rank(),
                                   score=0)
            profile.save()
            return profile

    def update(self):
        valid_subs = TaskSubmission.objects.filter(submitted_by=self.user,
                                                   valid=True)
        completed_tasks = set([x.task for x in valid_subs])
        self.score = sum([x.points_reward for x in completed_tasks])
        self.current_rank = Ranking.objects.filter(
            required_score__lte=self.score).order_by(
                '-required_score').first()
        self.save()


class CompilerProfile(models.Model):
    compile_cmd = models.CharField(max_length=100)
    execute_cmd = models.CharField(max_length=100)


class TaskSubmission(models.Model):
    NOT_EVALUATED = 0
    QUEUED = 1
    RUNNING = 2
    EVALUATED = 3
    STATES = (
        (NOT_EVALUATED, 'Ikke vurdert'),
        (QUEUED, 'Venter'),
        (RUNNING, 'Vurderes'),
        (EVALUATED, 'Vurdert'),
    )

    task = models.ForeignKey(Task)
    valid = models.BooleanField()
    content_file = models.FileField(upload_to='submissions/')
    submitted_by = models.ForeignKey(User)
    status = models.PositiveIntegerField(choices=STATES, default=NOT_EVALUATED)

    def execute(self, input=""):
        pass

    def save(self, *args, **kwargs):
        super(TaskSubmission, self).save(*args, **kwargs)
        ScoreProfile.objects.get(user=self.submitted_by).update()


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
