from django.shortcuts import render

def tasklist(request):
    return render(request, 'tasks/list.html')
