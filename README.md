#Siga os comandos abaixo no terminal:

virtualenv venv

cd venv/Scripts

activate



pip install django djangorestframework 

pip install mysqlclient

pip install django-cors-headers


cd TodoList


python manage.py makemigrations

python manage.py migrate

python manage.py runserver

