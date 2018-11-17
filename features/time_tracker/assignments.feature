Feature: Asignaciones
  Scenario: Asignar un empleado a un proyecto
    Given Existe un empleado, y existe un proyecto al cual no pertenece
    When Se lo asigna al proyecto
    Then Figura en la lista de de empleados asignados

  Scenario: Asignar un empleado a una tarea
    Given Existe un empleado en un proyecto, y existe una tarea a la que no esta asignado
    When Se lo asigna a la tarea
    Then Se crea una asignacion de tarea entre el empleado y esta

  Scenario: Asignar un empleado a una tarea
    Given Existe un empleado en un proyecto, y existe una tarea a la que no esta asignado
    When Se lo asigna a la tarea
    Then La asignacion inicialmente tiene cero horas invertidas

  Scenario: No se puede asignar un empleado a una tarea de un proyecto al cual no esta asignado
    Given Existe un empleado, y existe un proyecto con tareas al cual no esta asignado
    When Se intenta asignar el empleado a la tarea
    Then Ocurre una excepcion