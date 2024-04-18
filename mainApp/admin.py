from django.contrib import admin
from .models import *

# Registra o modelo ToDo no painel de administração
admin.site.register(ToDo)
