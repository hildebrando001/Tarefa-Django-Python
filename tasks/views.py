from django.shortcuts import render, get_object_or_404
from .models import Task

def tasklist(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/list.html',{'tasks':tasks})

def taskview(request,id):
    task = get_object_or_404(Task,pk=id)
    return render(request, 'tasks/task.html',{'task':task})