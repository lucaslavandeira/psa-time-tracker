from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    description = models.CharField(max_length=120)
    hours_estimated = models.IntegerField()
    hours_spent = models.IntegerField()

    def __str__(self):
        return f'{self.description} ({self.project})'


class Employee(models.Model):
    assigned_projects = models.ManyToManyField(Task, blank=True)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
