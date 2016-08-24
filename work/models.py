import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=32, unique=True)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=1024)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return "name: {}, start: {}, end: {}".format(self.name, self.start_date, self.end_date)

class WorkDivision(models.Model):
    name = models.CharField(max_length=1024)
    project = models.ForeignKey(Project, null=True, blank=True)

    def __str__(self):
        return self.name

class Work(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField()
    duration = models.IntegerField(default=0)
    project = models.ForeignKey(Project)
    division = models.ForeignKey(WorkDivision)

    def __str__(self):
        return "name: {}, date: {}, duration: {}".format(self.user, self.date, self.duration)
