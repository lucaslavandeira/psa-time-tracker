Feature: Asignaciones
  Scenario: Registrar un nuevo empleado
    When Se registra un nuevo empleado
    Then Inicialmente no esta asignado a ningun proyecto

  Scenario: Crear una nueva tarea
    Given Existe un proyecto
    When Se crea una nueva tarea en el proyecto
    Then Figura en la lista de tareas del proyecto

  Scenario: Crear una nueva tarea (horas iniciales)
    Given Existe un proyecto
    When Se crea una nueva tarea en el proyecto
    Then Las horas invertidas iniciales de la tarea son cero