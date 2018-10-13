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

Instalar dependencias: `pip install -r requirements.txt`

## Correr el proyecto

Correr el proyecto: `./manage.py runserver`

Verificar que se levanto bien yendo a `http://localhost:8000` en un browser
