from datetime import datetime
from django.utils import timezone

from django.conf import settings
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    description = models.CharField(max_length=120)
    hours_estimated = models.IntegerField()

    def __str__(self):
        return f'{self.description} ({self.project})'

    def get_hours(self):
        hours = [assignment.hours_spent for assignment in self.taskassignment_set.all()]
        return sum(hours)

    def is_over_limit(self) -> bool:
        return self.get_hours() > self.hours_estimated


class Employee(models.Model):
    assigned_projects = models.ManyToManyField(Project, blank=True)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    def assign_to_task(self, task: Task):
        if task.project not in self.assigned_projects.all():
            raise ValueError(f"La tarea {task} no pertenece a un proyecto al cual el empleado {self.name} este asignado")

        return self.taskassignment_set.create(task=task)

    def get_hours_worked(self, date: datetime = None):
        if date is None:
            date = timezone.now()

        date_assigments = self.taskassignment_set.filter(taskwork__date=date.date())
        return sum([assignment.hours_spent for assignment in date_assigments])


class TaskAssignment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def spend_hours(self, hours: int, date: datetime = None):
        if date is None:
            date = timezone.now()

        new_hours_worked_on_date = self.employee.get_hours_worked(date) + hours
        if new_hours_worked_on_date > settings.WORK_DAY_HOURS:
            raise ValueError

        task_work = self.taskwork_set.get_or_create(date=date.date(), defaults={'hours_spent': 0})[0]
        task_work.hours_spent = task_work.hours_spent + hours
        task_work.save()

    @property
    def hours_spent(self):
        work_hours = self.taskwork_set.all().values_list('hours_spent', flat=True)
        return sum(work_hours)


class TaskWork(models.Model):
    task_assignment = models.ForeignKey(TaskAssignment, on_delete=models.PROTECT)
    date = models.DateField()
    hours_spent = models.IntegerField()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.date > timezone.now().date():
            raise ValueError

        if self.hours_spent > settings.WORK_DAY_HOURS:
            raise ValueError

        super(TaskWork, self).save(force_insert, force_update, using, update_fields)
