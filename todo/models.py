from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
# Create your models here.


class Folder(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.name



class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.TimeField(default=datetime.time(0,0),null=True,blank=True)
    start_date = models.DateField(default = datetime.date.today,null=True,blank=True)
    end_time = models.TimeField(default=datetime.time(0,0),null=True,blank=True)
    deadline = models.DateField(blank=True,null=True)
    finished = models.BooleanField(default=False)
    folder = models.ForeignKey(Folder,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    priority = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def tasks(self):
        return self.task_set.filter(finished=False).order_by('deadline')

    def completed_tasks(self):
        return self.task_set.filter(finished=True).order_by('deadline')

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    start_time = models.TimeField(default=datetime.time(0,0),null=True,blank=True)
    start_date = models.DateField(default = datetime.date.today,null=True,blank=True)
    end_time = models.TimeField(default=datetime.time(0,0),null=True,blank=True)
    deadline = models.DateField(blank=True,null=True)
    completed_date = models.DateField(blank=True,null=True)
    finished = models.BooleanField(default=False)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    hidden  = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def color(self):
        if(self.finished):
            return "green"
        return "red"

    def __str__(self):
        return self.name
