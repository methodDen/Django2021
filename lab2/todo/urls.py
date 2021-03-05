from django.urls import path
from todo.views import uncompleted_list_show, completed_list_show

urlpatterns = [
    path('<int:list_id>/uncompleted/', uncompleted_list_show, name="uncompleted_list_show"),
    path('<int:list_id>/completed/', completed_list_show, name="completed_list_show")

]
