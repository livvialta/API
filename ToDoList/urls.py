"""
URL configuration for ToDoList project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Importa o módulo admin do Django para lidar com as rotas de administração
# e o módulo include para incluir as rotas do aplicativo principal
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Define a rota para o painel de administração do Django
    path('admin/', admin.site.urls),
    
    # Define a rota para as URLs do API do aplicativo principal
    path('api/', include('mainApp.urls'))
]


