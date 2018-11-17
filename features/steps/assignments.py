from behave import *

from apps.tracking.models import Employee, Project, Task

use_step_matcher("re")


@given("Existe un empleado, y existe un proyecto al cual no pertenece")
def step_impl(context):
    context.project = Project.objects.create(name='Proyecto ejemplo')
    context.employee = Employee.objects.create(name='Lucas Lavandeira')


@when("Se lo asigna al proyecto")
def step_impl(context):
    context.employee.assigned_projects.add(Project.objects.first())


@then("Figura en la lista de de empleados asignados")
def step_impl(context):
    employees = context.project.employee_set.all()
    assert context.employee in set(employees)


@when("Se lo asigna a la tarea")
def step_impl(context):
    context.employee.assign_to_task(Task.objects.first())


@then("Se crea una asignacion de tarea entre el empleado y esta")
def step_impl(context):
    assignment = context.employee.taskassignment_set.first()
    assert assignment.employee == Employee.objects.first()
    assert assignment.task == Task.objects.first()


@when("Se intenta asignar el empleado a la tarea")
def step_impl(context):
    try:
        context.employee.assign_to_task(Task.objects.first())
        context.e = None
    except ValueError as e:
        context.e = e


@then("Ocurre una excepcion")
def step_impl(context):
    assert isinstance(context.e, ValueError)


@then("La asignacion inicialmente tiene cero horas invertidas")
def step_impl(context):
    assert context.employee.taskassignment_set.first().hours_spent == 0


@given("Existe un empleado en un proyecto, y existe una tarea a la que no esta asignado")
def step_impl(context):
    context.project = Project.objects.create(name='Proyecto ejemplo')
    context.employee = Employee.objects.create(name='Lucas Lavandeira')
    context.employee.assigned_projects.add(context.project)
    context.project.task_set.create(description='Tarea ejemplo', hours_estimated=10)

