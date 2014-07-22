from django.db import models

#Represents a program that can be compiled and executed
class Program(models.Model):
    source      = models.CharField(max_length=400)
    compiler    = models.ForeignKey(CompilerProfile)

#Simple string comparison
class BasicTest(models.Model):
    input = models.CharField(max_length=400)
    output= models.CharField(max_length=400)

#Lets an external program assess output correctness
class ProgramTest(BasicTest):
    program = models.ForeignKey(Program)

class CompilerProfile(models.Model):
    compile = models.CharField(max_length=100)
    run     = models.CharField(max_length=100)
    usertime= models.PositiveIntegerField()

#A task for users to solve
class Task(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=400)
    time_stamp = models.DateTimeField(auto_add_now=True)

#An attempt at solving a problem
class Submission(models.Model):
    task    = models.ForeignKey(Task)
    program = models.ForeignKey(Program)
    time_stamp = models.DateTimeField(auto_add_now=True)

