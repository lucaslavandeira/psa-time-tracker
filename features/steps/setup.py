from behave import *

from apps.tracking.models import Employee, Project, Task, TaskAssignment

use_step_matcher("re")


@when('Se registra un nuevo empleado')
def step_impl(context):
    context.employee = Employee.objects.create(name='Test employee')


@then('Inicialmente no esta asignado a ningun proyecto')
def step_impl(context):
    employee = context.employee
    assert employee.assigned_projects.count() == 0


@given("Existe un empleado, y existe un proyecto con tareas al cual no esta asignado")
def step_impl(context):
    context.employee = Employee.objects.create(name='Lucas Lavandeira')
    context.project = Project.objects.create(name='Proyecto ejemplo')
    context.project.task_set.create(description='Tarea ejemplo', hours_estimated=10)


@given("Existe un proyecto")
def step_impl(context):
    context.project = Project.objects.create(name='Test Project')


@when("Se crea una nueva tarea en el proyecto")
def step_impl(context):
    context.task = context.project.task_set.create(description='Tarea ejemplo', hours_estimated=10)


@then("Figura en la lista de tareas del proyecto")
def step_impl(context):
    assert context.task in context.project.task_set.all()


@then("Las horas invertidas iniciales de la tarea son cero")
def step_impl(context):
    assert context.task.get_hours() == 0
