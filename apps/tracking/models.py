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

    @property
    def hours_spent(self):
        hours = [assignment.hours_spent for assignment in self.taskwork_set.all()]
        return sum(hours)

    def is_over_limit(self) -> bool:
        return self.hours_spent > self.hours_estimated


class Employee(models.Model):
    name = models.CharField(max_length=64)
    assigned_projects = models.ManyToManyField(Project, blank=True)
    assigned_tasks = models.ManyToManyField(Task, blank=True)

    def __str__(self):
        return self.name

    def assign_to_task(self, task: Task):
        if task.project not in self.assigned_projects.all():
            msg = f"La tarea {task} no pertenece a un proyecto al cual el empleado {self.name} este asignado"
            raise ValueError(msg)

        self.assigned_tasks.add(task)

    def get_hours_worked(self, date: datetime = None):
        if date is None:
            date = timezone.now()

        if isinstance(date, datetime):
            date = date.date()

        date_assigments = self.taskwork_set.filter(date=date)
        return sum([assignment.hours_spent for assignment in date_assigments])

    def spend_hours(self, task: Task, hours: int, date: datetime = None):
        if task not in self.assigned_tasks.all():
            raise ValueError(f"El empleado {self.name} no esta asignado a la tarea {task}")

        if date is None:
            date = timezone.now()

        new_hours_worked_on_date = self.get_hours_worked(date) + hours
        if new_hours_worked_on_date > settings.WORK_DAY_HOURS:
            raise ValueError("La cantidad de horas a cargar superaria el maximo de horas laborales diaria")

        if isinstance(date, datetime):
            date = date.date()
        task_work = self.taskwork_set.get_or_create(task=task, date=date, defaults={'hours_spent': 0})[0]
        task_work.hours_spent = task_work.hours_spent + hours
        task_work.save()

    @classmethod
    def get_from_session(cls):
        # Not implemented: getting Employee from the currently logged in user
        return Employee.objects.first()


class TaskWork(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    task = models.ForeignKey(Task, on_delete=models.PROTECT)
    date = models.DateField()
    hours_spent = models.IntegerField()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.date > timezone.now().date():
            raise ValueError("La fecha cargada es en el futuro")

        if self.hours_spent > settings.WORK_DAY_HOURS:
            raise ValueError("La cantidad de horas a cargar superaria el maximo de horas laborales diaria")

        super(TaskWork, self).save(force_insert, force_update, using, update_fields)
