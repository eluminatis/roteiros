# Instalação basica de um projeto em python/django
Para esse exemplo vamos usar *wttd* como nome do diretorio de trabalho e *eventex* como nome do projeto

*Para facilitar sua vida crie o seguinte alias em seu bashrc ou zshrc*

    alias manage='python $VIRTUAL_ENV/../manage.py'

## Criando o projeto
crie a pasta do projeto e entre nela

    mkdir wttd
    cd wttd

crie o venv

    # Como boa prática, utilizar o nome venv ou .venv
    python -m venv .venv

ative o `venv`

    source .wttd/bin/activate

instale o django

    pip install django

inicialize o projeto

    django-admin startproject eventex .

entre no projeto e crie a app núcleo do projeto

    cd eventex
    manage startapp core

no arquivo *wttd/eventex/settings.py* adicione a lista INSTALLED_APPS o app que vc acabou de criar para o projeto reconhecê-lo

    'eventex.core',

no arquivo *eventex/urls.py* importe as views do core e adicione a rota que sera atendida por seu metodo **home**

```python
    import eventex.core.views
    ...
    path('', eventex.core.views.home),
```

no arquivo *eventex/core/views.py* adicione o método que atenderá essa rota

```python
    def home(request):
        return render(request, 'index.html')
```

perceba que o metodo home chama o arquivo index.html que é um template, crie uma pasta *templates/* dentro de *core/* e coloque seu *index.html* la

ainda na pasta *core/* crie a pasta *static/* e coloque todos os arquivos estaticos dos quais seu template depende dentro dela

nas chamadas para arquivos estaticos substitua o caminha relativo pela função statis do python

```python
    para fins de exemplo substitua todas as strings do tipo
    "img/favicon.ico"
    por
    {% static 'img/favicon.ico' %}
```

## separando configurações por instância e servindo arquivos estáticos de forma mais perfomática

em *wttd/* instale as dependencias: python-decouple, dj-database-url e dj-static

    pip install python-decouple
    pip install dj-database-url
    pip install dj-static

configurar o arquivo settings.py e o arquivo .env

#### arquivo *eventex/settings.py*

faça as substituições:

```python
    import os
    from decouple import config
    from dj_database_url import parse as dburl
    ...
    ALLOWED_HOSTS = ['*']

    SECRET_KEY = config('SECRET_KEY')

    DEBUG = config('DEBUG', default=False, cast=bool)

    default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    DATABASES = {
    'default': config('DATABASE_URL', default=default_dburl, cast=dburl),
    }

    LANGUAGE_CODE = 'pt-br'

    TIME_ZONE = 'America/Sao_Paulo'

    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

#### arquivo *wttd/.env*

crie o arquivo .env na pasta raiz do projeto e adicione:

    SECRET_KEY=#coloque_aqui_sua_secret_key (sem espaços nem aspas)
    DEBUG=True

#### arquivo *eventex/wsgi.py*

importe o Cling e envolva o get_wsgi_application() com ele

```python
    from dj_static import Cling
    ...
    application = Cling(get_wsgi_application())
```

#### exportando as dependencias do projeto

    pip freeze > requirements.txt

## Preparando o projeto para o Heroku

no *wttd/requirements.txt* adicione as seguintes dependencias

    gunicorn==19.8.1
    psycopg2==2.7.4

#### em *wttd/* crie o arquivo Procfile com o seguinte conteudo

    web: gunicorn eventex.wsgi --log-file -

## Inicializando o repositório git

em *wttd/*

    git init

ainda em *wttd/* crie o arquivo .gitignore e adicione o seguinte conteudo

    .env            //seu .env local
    .vscode         //arquivos de sua ide
    .wttd           //seu venv
    *.sqlite3       //bd de dev
    *.pyc           //arquivos compilados
    __pycache__     //cache de arquivos compilados do python

add o .gitignore a seu projeto, faça commit e em seguida adicione todo o resto

## criando uma app no heroku e colocando seu projeto no ar

    heroku apps:create eventex-petersonpassos
    heroku config:set SECRET_KEY='sua_key_entre_aspas_simples'
    heroku config:set DEBUG=False
    git push heroku master --force

## começando a trabalhar com banco de dados e o admin do django

roda as migrations

    manage migrate

crie o super usuário

    manage createsuperuser

pronto, já pode acessar o admin do django em http://127.0.0.1:8000/admin/
