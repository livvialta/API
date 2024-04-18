#Siga os comandos abaixo no terminal:

virtualenv venv

cd venv/Scripts

activate



pip install django djangorestframework mysqlserver


cd TodoList


python manage.py makemigrations

python manage.py migrate

python manage.py runserver

