from django.urls import path
from todo.views import uncompleted_list_show, completed_list_show, completed_task, uncompleted_task

urlpatterns = [
    path('uncompleted/', uncompleted_list_show, name="uncompleted_list_show"),
    path('completed/', completed_list_show, name="completed_list_show"),
    path('completed/<int:task_id>', completed_task, name="completed_task"),
    path('uncompleted/<int:task_id>', uncompleted_task, name="uncompleted_task"),

]
