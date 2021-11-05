from django.db import models
from django.db.models.deletion import CASCADE
# Create your models here.


class Work(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    due_date = models.DateTimeField(auto_now=False, auto_now_add=False)

    def get_absolute_url(self):
        return "/work/"

    def __str__(self):
        return f"{self.name}"


class Schedule(models.Model):
    class_name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    time = models.TimeField(auto_now=False, auto_now_add=False)

    def get_absolute_url(self):
        return "/schedule/"

    def __str__(self):
        return f"{self.class_name}"


class CheckList(models.Model):
    check_name = models.ForeignKey(Work, on_delete=CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return "/checklist/"

    def __str__(self):
        return f"{self.check_name}"
