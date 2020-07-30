from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm, TaskFormEdit


def taskList(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/list.html',{'tasks':tasks})


def taskView(request,id):
    task = get_object_or_404(Task,pk=id)
    return render(request, 'tasks/task.html',{'task':task})


def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'novo'
            task.save()
            return redirect("/")
    else:
        form = TaskForm()
        return render(request, 'tasks/addtask.html',{'form':form})


def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskFormEdit(instance=task)

    if (request.method == 'POST'):
        form = TaskFormEdit(request.POST, instance=task)
        if form.is_valid():
            task.save()
            return redirect('/')
        else:
            return render(request, 'tasks/edittask.html', {'task':task, 'form':form})

    else:
        return render(request, 'tasks/edittask.html', {'task':task, 'form':form})


def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    return redirect('/')


