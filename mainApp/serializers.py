from rest_framework import serializers 
from .models import *

class TToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('id', 'Title', 'Description', 'Price', 'Completed')

        