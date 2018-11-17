from django.utils import timezone

from behave import given, when, then
from dateutil.relativedelta import relativedelta

from apps.tracking.models import Project, Task, Employee


@given("Existe un empleado con tareas dentro de un proyecto")
def step_impl(context):
    project = Project.objects.create(name='Proyecto ejemplo')
    context.task = Task.objects.create(project=project, description='Tarea ejemplo', hours_estimated=10)
    context.employee = Employee.objects.create(name='Lucas Lavandeira')
    context.employee.assigned_projects.add(project)
    context.employee.assign_to_task(context.task)


@when("El empleado carga una hora a la tarea")
def step_impl(context):
    context.employee.spend_hours(context.task, 1)


@then("La tarea tiene una hora invertida")
def step_impl(context):
    assert Task.objects.first().hours_spent == 1


@when("El empleado intenta cargar horas en la tarea")
def step_impl(context):
    try:
        context.employee.spend_hours(context.task, 1)
        context.e = None

    except ValueError as e:
        context.e = e


@then("Ocurre una excepcion de que no existe la asignacion")
def step_impl(context):
    assert isinstance(context.e, ValueError)


@when("El empleado carga horas en dos dias diferentes")
def step_impl(context):
    context.employee.spend_hours(context.task, 1)
    yesterday = timezone.now() - relativedelta(days=1)
    context.employee.spend_hours(context.task, 1, yesterday)


@then("El empleado invirtio unas horas totales iguales a la suma de ambos dias")
def step_impl(context):
    assert context.task.hours_spent == 2


@when("El empleado intenta cargar horas en un dia futuro")
def step_impl(context):
    tomorrow = timezone.now() + relativedelta(days=1)
    try:
        context.employee.spend_hours(context.task, 1, tomorrow)
    except Exception as e:
        context.e = e


@when("El empleado intenta cargar mas horas que su dia laboral (8 horas)")
def step_impl(context):
    try:
        context.employee.spend_hours(context.task, 9)
    except Exception as e:
        context.e = e


@when("El empleado carga horas dos veces en una misma tarea")
def step_impl(context):
    context.employee.spend_hours(context.task, 1)
    context.employee.spend_hours(context.task, 2)


@then("Las horas invertidas en esa tarea para ese dia es la suma de ambas cargas")
def step_impl(context):
    assert context.employee.taskwork_set.first().hours_spent == 3


@given("Existen dos empleados asignados a la misma tarea dentro de un proyecto")
def step_impl(context):
    project = Project.objects.create(name='Proyecto ejemplo')
    context.task = Task.objects.create(project=project, description='Tarea ejemplo', hours_estimated=10)
    context.first_employee = Employee.objects.create(name='Lucas Lavandeira')
    context.first_employee.assigned_projects.add(project)
    context.first_employee.assign_to_task(context.task)

    context.second_employee = Employee.objects.create(name="Matias Reimondo")
    context.second_employee.assigned_projects.add(project)
    context.second_employee.assign_to_task(context.task)


@when("Ambos cargan horas a la tarea")
def step_impl(context):
    context.first_employee.spend_hours(context.task, 1)
    context.second_employee.spend_hours(context.task, 2)


@then("Las horas invertidas en esa tarea es la suma de las cargas de ambos empleados")
def step_impl(context):
    assert context.task.hours_spent == 3


@when("Uno carga horas a la tarea y el otro no")
def step_impl(context):
    context.first_employee.spend_hours(context.task, 1)


@then("Las horas invertidas del otro siguen siendo cero")
def step_impl(context):
    assert context.second_employee.get_hours_worked() == 0


@when("Ambos cargan horas a la tarea en distintos dias")
def step_impl(context):
    context.first_employee.spend_hours(context.task, 1)
    yesterday = timezone.now() - relativedelta(days=1)
    context.second_employee.spend_hours(context.task, 2, yesterday)


@given("Existe un empleado con dos tareas dentro de un proyecto")
def step_impl(context):
    project = Project.objects.create(name='Proyecto ejemplo')
    context.first_task = Task.objects.create(project=project, description='Tarea ejemplo', hours_estimated=10)
    context.employee = Employee.objects.create(name='Lucas Lavandeira')
    context.employee.assigned_projects.add(project)
    context.employee.assign_to_task(context.first_task)
    context.second_task = Task.objects.create(project=project, description='Otra tarea ejemplo', hours_estimated=10)
    context.employee.assign_to_task(context.second_task)


@when("El empleado intenta cargar mas horas que un dia laboral, separadas en las dos tareas")
def step_impl(context):
    try:
        context.employee.spend_hours(context.first_task, 5)
        context.employee.spend_hours(context.second_task, 5)
    except Exception as e:
        context.e = e


@then("El empleado tiene una hora trabajada para el dia actual")
def step_impl(context):
    assert context.employee.get_hours_worked() == 1


@when("El empleado carga horas en ambas tareas")
def step_impl(context):
    context.employee.spend_hours(context.first_task, 1)
    context.employee.spend_hours(context.second_task, 2)


@then("Las horas trabajadas del empleado para el dia actual es la suma de ambas cargas")
def step_impl(context):
    assert context.employee.get_hours_worked() == 3


@then("Las horas invertidas de las tareas estan por debajo de la estimacion")
def step_impl(context):
    assert not context.task.is_over_limit()


@when("El empleado carga mas horas de las estimadas a la tarea")
def step_impl(context):
    yesterday = timezone.now() - relativedelta(days=1)
    context.employee.spend_hours(context.task, 8, yesterday)
    context.employee.spend_hours(context.task, 8)


@then("La tarea tendra tiempo invertido por encima del limite")
def step_impl(context):
    assert context.task.is_over_limit()


@when("El empleado carga una hora a la tarea el dia anterior")
def step_impl(context):
    yesterday = timezone.now() - relativedelta(days=1)
    context.employee.spend_hours(context.task, 1, yesterday)


@then("Las horas trabajadas del dia de hoy son cero")
def step_impl(context):
    assert context.employee.get_hours_worked() == 0
