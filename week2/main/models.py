from django.db import models
from users.models import MainUser
from datetime import datetime

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    status = models.BooleanField()
    creator = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='projects')

class Block(models.Model):
    name = models.CharField(max_length=255)
    type_of = models.IntegerField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='blocks')

class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    priority = models.IntegerField()
    creator = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='created_tasks')
    executor = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='tasks')
    block = models.ForeignKey(Block, on_delete=models.CASCADE, related_name='tasks')
    order = models.IntegerField()

class TaskDocument(models.Model):
    document = models.FileField()
    creator = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='docs')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='docs')

class TaskComment(models.Model):
    body = models.CharField(max_length=10000)
    creator = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='docs')
    created_at = models.DateTimeField(default=datetime.datetime.now)