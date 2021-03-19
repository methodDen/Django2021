from django.shortcuts import render
from rest_framework import viewsets
from main.models import Task, TodoList
from main.serializers import TaskSerializer, TodoListSerializer, TodoListWithoutTasksSerializer, SimpleTaskSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
# Create your views here.


class TodoListViewSet(viewsets.ModelViewSet):

    queryset = TodoList.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'update', 'create']:
            return TodoListWithoutTasksSerializer
        if self.action == 'retrieve':
            return TodoListSerializer

    def get_permissions(self): #
        if self.action == 'list':
            permission_classes = (AllowAny,)
        else:
            permission_classes = (IsAuthenticated,)

        return [permission() for permission in permission_classes]

    @action(methods=['GET'], detail=True)
    def completed_list(self, request, **kwargs):
        target_id = int(kwargs['todo_list_id'])
        todo = TodoList.objects.get(pk=target_id)
        queryset = todo.tasks.filter(mark=True)
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)


class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all()

    def get_permissions(self): #
        if self.action == 'list':
            permission_classes = (AllowAny,)
        else:
            permission_classes = (IsAuthenticated,)

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'list':
            return SimpleTaskSerializer
        else:
            return TaskSerializer