from lib2to3.pgen2 import token
from telnetlib import DO
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework.authtoken.models import Token

class OwnedModel(models.Model):
    owner= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    class Meta:
        abstract = True

class Belonging(OwnedModel):
    name= models.CharField(max_length=100)

class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    # If there are any fields needed add here.

    def __str__(self):
        return self.username


class Project(TimestampModel):
    title = models.CharField(max_length=128)
    description = models.TextField()
    code = models.CharField(max_length=64, unique=True, null=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=int(1))
    def __str__(self):
        return "{0} {1}".format(self.code, self.title)


class Issue(TimestampModel):
    BUG = "BUG"
    TASK = "TASK"
    STORY = "STORY"
    EPIC = "EPIC"
    TYPES = [(BUG, BUG), (TASK, TASK), (STORY, STORY), (EPIC, EPIC)]

    OPEN = "OPEN"
    INPROGRESS = "INPROGRESS"
    INREVIEW = "INREVIEW"
    CODECOMPLETE = "CODECOMPLETE"
    QATESTING = "QATESTING"
    DONE = "DONE"
    STATUS = [(OPEN,OPEN), (INPROGRESS, INPROGRESS), (INREVIEW, INREVIEW), (CODECOMPLETE, CODECOMPLETE), (QATESTING, QATESTING), (DONE, DONE)]

    title = models.CharField(max_length=128)
    description = models.TextField()

    type = models.CharField(max_length=8, choices=TYPES, default=BUG, null=False)

    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="issues", null=False
    )
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reporter", null=False,default=int(1), editable=False)
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assignee", default=int(1))
    status = models.CharField(max_length=16, choices=STATUS, default=OPEN, null= False)
    def __str__(self):
        return "{0}-{1}".format(self.project.code, self.title)
