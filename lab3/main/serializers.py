from rest_framework import serializers
from main.models import TodoList, Task
from drf_writable_nested.serializers import WritableNestedModelSerializer

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'

class SimpleTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('name', 'dateOfCreation', 'deadlineDate', 'mark')

class TodoListSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)

    class Meta:
        model = TodoList
        fields = '__all__'


class TodoListWithoutTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ('name', 'dateOfCreation')

