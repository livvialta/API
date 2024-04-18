from rest_framework import serializers 
from .models import *

class TToDoSerializer(serializers.ModelSerializer):
    class Meta:
        # Define o modelo que será serializado
        model = ToDo
        
        # Define os campos do modelo que serão incluídos na serialização
        fields = ('id', 'Title', 'Description', 'Price', 'Completed')
