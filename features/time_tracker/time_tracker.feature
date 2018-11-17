Feature: Carga de horas
  Scenario: Cargar horas a una tarea
    Given Existe un empleado con tareas dentro de un proyecto
    When El empleado carga una hora a la tarea
    Then La tarea tiene una hora invertida

  Scenario: No se puede cargar horas a una tarea a la que no estoy asignado
    Given Existe un empleado en un proyecto, y existe una tarea a la que no esta asignado
    When El empleado intenta cargar horas en la tarea
    Then Ocurre una excepcion de que no existe la asignacion

  Scenario: Cargar horas a una tarea en dias diferentes
    Given Existe un empleado con tareas dentro de un proyecto
    When El empleado carga horas en dos dias diferentes
    Then El empleado invirtio unas horas totales iguales a la suma de ambos dias

  Scenario: Intentar cargar horas en un dia futuro
    Given Existe un empleado con tareas dentro de un proyecto
    When El empleado intenta cargar horas en un dia futuro
    Then Ocurre una excepcion

  Scenario: Intentar cargas mas horas que un dia laboral
    Given Existe un empleado con tareas dentro de un proyecto
    When El empleado intenta cargar mas horas que su dia laboral (8 horas)
    Then Ocurre una excepcion

  Scenario: Cargar horas dos veces para el mismo dia
    Given Existe un empleado con tareas dentro de un proyecto
    When El empleado carga horas dos veces en una misma tarea
    Then Las horas invertidas en esa tarea para ese dia es la suma de ambas cargas

  Scenario: Dos empleados cargan horas en la misma tarea
    Given Existen dos empleados asignados a la misma tarea dentro de un proyecto
    When Ambos cargan horas a la tarea
    Then Las horas invertidas en esa tarea es la suma de las cargas de ambos empleados

  Scenario: Un empleado carga horas a una tarea y el otro no
    Given Existen dos empleados asignados a la misma tarea dentro de un proyecto
    When Uno carga horas a la tarea y el otro no
    Then Las horas invertidas del otro siguen siendo cero

  Scenario: Dos empleados cargan horas en la misma tarea en distintos dias
    Given Existen dos empleados asignados a la misma tarea dentro de un proyecto
    When Ambos cargan horas a la tarea en distintos dias
    Then Las horas invertidas en esa tarea es la suma de las cargas de ambos empleados

  Scenario: Un empleado intenta cargar mas horas que un dia laboral en dos tareas
    Given Existe un empleado con dos tareas dentro de un proyecto
    When El empleado intenta cargar mas horas que un dia laboral, separadas en las dos tareas
    Then Ocurre una excepcion

  Scenario: Un empleado carga horas en una tarea
    Given Existe un empleado con tareas dentro de un proyecto
    When El empleado carga una hora a la tarea
    Then El empleado tiene una hora trabajada para el dia actual

  Scenario: Un empleado carga horas en dos tareas diferentes
    Given Existe un empleado con dos tareas dentro de un proyecto
    When El empleado carga horas en ambas tareas
    Then Las horas trabajadas del empleado para el dia actual es la suma de ambas cargas

  Scenario: Un empleado carga horas en una tarea el dia anterior
    Given Existe un empleado con tareas dentro de un proyecto
    When El empleado carga una hora a la tarea el dia anterior
    Then Las horas trabajadas del dia de hoy son cero

  Scenario: Tarea con horas cargadas debajo de la estimacion
    Given Existe un empleado con tareas dentro de un proyecto
    When El empleado carga una hora a la tarea
    Then Las horas invertidas de las tareas estan por debajo de la estimacion

  Scenario: Tarea con horas cargadas por encima de la estimacion
    Given Existe un empleado con tareas dentro de un proyecto
    When El empleado carga mas horas de las estimadas a la tarea
    Then La tarea tendra tiempo invertido por encima del limite