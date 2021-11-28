from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Taskserializers,UserSerializer
from .models import Task
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView 

# Create your views here.

class TaskViewset(viewsets.ModelViewSet):
    Permission_clasess = (IsAuthenticated,)
    queryset = Task.objects.all().order_by('-date_created')
    serializer_class = Taskserializers


class DueTaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date_created').filter(completed=False)
    serializer_class = Taskserializers


class CreateUserView(CreateAPIView):
    model = get_user_model()
    Permission_clasess = (AllowAny,)
    serializer_class = UserSerializer

class CompletedTaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date_created').filter(completed=True)
    serializer_class = Taskserializers    