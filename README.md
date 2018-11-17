# PSA time-tracker

## Instalacion

Ver [`pyenv`](https://github.com/pyenv/pyenv).

Mac: Usar Homebrew

Linux:

Instalar dependencias (Debian, Ubuntu):
```
apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev
```
Instalar pyenv: 

`curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash`

Instalar Python 3.7.0
`pyenv install 3.7.0`

Configurar el entorno virtual para el proyecto:
`pyenv virtualenv 3.7.0 aninfo`

Luego clonar este repositorio, y activar el entorno virtual de python 3.7 creando un archivo `.python-version` con contenidos `aninfo`: `echo "aninfo" > .python.version`.

Instalar dependencias: `pip install -r requirements.txt`

## Correr el proyecto

Correr el proyecto: `./manage.py runserver`

Verificar que se levanto bien yendo a `http://localhost:8000` en un browser.

Como está fuera de alcance el alta de proyectos, tareas, y empleados, se pueden generar a través de la UI del Admin de Django. Para ello, crear una cuenta de superusuario: `./manage.py createsuperuser`, y seguir las instrucciones. Luego, desde `http://localhost:8000/admin` se puede utilizar la interfaz visual para crear los modelos necesarios.

