from django.urls import path
from todo.views import uncompleted_list_show, completed_list_show

urlpatterns = [
    path('uncompleted/', uncompleted_list_show),
    path('completed/', completed_list_show)
]
