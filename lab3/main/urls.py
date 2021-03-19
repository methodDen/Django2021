from main.views import TodoListViewSet, TaskViewSet
from rest_framework import routers
from django.urls import path

router = routers.SimpleRouter()
router.register('todos', TodoListViewSet, basename='main')
router.register('task', TaskViewSet, basename='main')
urlpatterns = [
    path('todos/<int:todo_list_id>/completed/', TodoListViewSet.as_view({'get': 'completed_list'}))
]

urlpatterns += router.urls