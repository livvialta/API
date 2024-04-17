from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

#CRUD Operations 

#read
class ListTodo(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = TToDoSerializer

#update 
class DetailTodo(generics.RetrieveUpdateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = TToDoSerializer

#create 
class CreateTodo(generics.CreateAPIView):
    queryset = ToDo.objects.all
    serializer_class = TToDoSerializer

#delete
class DeleteTodo(generics.DestroyAPIView): 
    queryset = ToDo.objects.all()
    serializer_class = TToDoSerializer