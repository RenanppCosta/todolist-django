from django.shortcuts import render, redirect
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
