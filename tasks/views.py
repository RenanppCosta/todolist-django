from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Task  
from .forms import TaskForm  

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('create_task')  
    else:
        form = TaskForm()  
    
    tasks = Task.objects.all() 
    return render(request, "index.html", {"form": form, "tasks": tasks})

def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('create_task')

def update_task(request):
        data_id = request.GET.get("data_id")
        title = request.GET.get("task_title")

        task = get_object_or_404(Task, id=data_id)
        task.title = title
        task.save()

        data = {"title": title, "status":"update_task"}
        return JsonResponse(data)