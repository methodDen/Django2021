from django.contrib import admin
from todo.models import Task
# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'dateOfCreation', 'deadlineDate', 'mark']
    ordering = ['dateOfCreation']
    search_fields = ['name']
    list_filter = ['dateOfCreation', 'deadlineDate', 'mark', 'ownerName']