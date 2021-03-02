from django.shortcuts import render
from .models import Task

# Create your views here.


def uncompleted_list_show(request):
    return render(request, "todo_list.html", {
        "tasks": Task.objects.filter(mark=False)
    })


def completed_list_show(request):
    return render(request, "completed_todo_list.html", {
        "tasks": Task.objects.filter(mark=True)
    })


def completed_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    return render(request, "completed.html", {
        "task": task
    })

def uncompleted_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    return render(request, "uncompleted.html", {
        "task": task
    })




