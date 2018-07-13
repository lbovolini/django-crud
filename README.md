# Walkthrough

install python
install pip
pip install pylint

## Criar virtualenv
python -m venv djangoenv

## Executar
source djangoenv/bin/activate

## Instalar Django
pip install django

pip freeze > requirements.txt

## Começar um novo projeto Django
django-admin startproject southpark

## Alterar time zone em settings.py e adicionar caminho para arquivos estaticos
'America/Sao_Paulo'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

## Criar bando de dados
python manage.py migrate

## Iniciar o servidor web para testar a aplicacao
python manage.py runserver

## Acessar o endereco
http://127.0.0.1:8000/

## Criar aplicativo 
python manage.py startapp app

## No arquivo southpark/settings.py, encontrar o INSTALLED_APPS e adicionar uma linha com 'app', logo acima do ).

## Criar modelo
## Atualizar mudancas
python manage.py makemigrations app
python manage.py migrate app

## Registrar model em app/admin.py

## Criar superuser
python manage.py createsuperuser

## Registrar url

# Links úteis

http://getbootstrap.com/docs/4.0/examples/carousel/#

https://blackrockdigital.github.io/startbootstrap-agency/

https://www.crazyegg.com/blog/website-color-palettes/

https://blackrockdigital.github.io/startbootstrap-full-slider/

https://stackoverflow.com/questions/36659031/edit-model-data-using-modelform-modelform-validation-error

https://bootsnipp.com/snippets/eNbOa

http://plugins.krajee.com/file-avatar-upload-demo

https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html

https://www.sitepoint.com/community/t/bootstrap-align-content-of-a-div-to-bottom/248173/16
