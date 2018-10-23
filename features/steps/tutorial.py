from behave import *
from apps.tracking.models import Employee


@given('we have behave installed')
def step_impl(context):
    context.test.client.get('/')

@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False


@when('Se registra un nuevo empleado')
def step_impl(context):
    Employee.objects.create(name='Test employee')


@then('Inicialmente no esta asignado a ningun proyecto')
def step_impl(context):
    employee = Employee.objects.first()
    assert employee.assigned_projects.count() == 0
