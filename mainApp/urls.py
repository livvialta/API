from django.urls import path
from .views import *

# Define os padrões de URL para as views do aplicativo
urlpatterns = [
    # Define o padrão de URL para visualizar detalhes de uma tarefa específica
    path('<int:pk>/', DetailTodo.as_view()),

    # Define o padrão de URL para listar todas as tarefas
    path('', ListTodo.as_view()),

    # Define o padrão de URL para criar uma nova tarefa
    path('create', CreateTodo.as_view()),

    # Define o padrão de URL para excluir uma tarefa específica
    path('delete/<int:pk>', DeleteTodo.as_view())
]
