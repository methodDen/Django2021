from django.shortcuts import render
from datetime import datetime

# Create your views here.
def uncompleted_list_show(request):

    tasks = [
        {
            'id': '1234',
            'name': 'Task 1',
            'created': datetime(2018, 9, 10).strftime("%d/%m/%Y"),
            'due': datetime(2018, 9, 12).strftime("%d/%m/%Y"),
            'owner': 'admin',
            'mark': 'done'
        },
        {
            'id': '1234',
            'name': 'Task 2',
            'created': datetime(2018, 9, 10).strftime("%d/%m/%Y"),
            'due': datetime(2018, 9, 12).strftime("%d/%m/%Y"),
            'owner': 'admin',
            'mark': 'done'
        },
        {
            'id': '1234',
            'name': 'Task 3',
            'created': datetime(2018, 9, 10).strftime("%d/%m/%Y"),
            'due': datetime(2018, 9, 12).strftime("%d/%m/%Y"),
            'owner': 'admin',
            'mark': 'done'
        },
        {
            'id': '1234',
            'name': 'Task 4',
            'created': datetime(2018, 9, 10).strftime("%d/%m/%Y"),
            'due': datetime(2018, 9, 12).strftime("%d/%m/%Y"),
            'owner': 'admin',
            'mark': 'done'
        }
    ]

    context = {
        'tasks': tasks
    }

    return render(request, 'todo_list.html', context=context)

def completed_list_show(request):
    tasks = [
        {
            'id': '1234',
            'name': 'Task 0',
            'created': datetime(2018, 9, 10).strftime("%d/%m/%Y"),
            'due': datetime(2018, 9, 12).strftime("%d/%m/%Y"),
            'owner': 'admin',
            'mark': 'Not done'
        }
    ]

    context = {
        'tasks': tasks
    }

    return render(request, 'completed_todo_list.html', context=context)

