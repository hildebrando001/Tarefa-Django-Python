from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm, TaskFormEdit
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required
def taskList(request):
    search = request.GET.get('search') # "search" is the NAME of the input search on list.html

    if search:
        tasks = Task.objects.filter(title__icontains=search, user=request.user)
    else:
        tasks_list = Task.objects.all().order_by('-created_at').filter(user=request.user)

        paginator = Paginator(tasks_list, 3)
        page = request.GET.get('page')
        tasks = paginator.get_page(page)

    return render(request, 'tasks/list.html',{'tasks':tasks})


@login_required
def taskView(request,id):
    task = get_object_or_404(Task,pk=id)
    return render(request, 'tasks/task.html',{'task':task})


@login_required
def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'novo'
            task.user = request.user
            task.save()
            return redirect("/")
    else:
        form = TaskForm()
        return render(request, 'tasks/addtask.html',{'form':form})


@login_required
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


@login_required
def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    messages.success(request, "Item deletado com sucesso")
    return redirect('/')


