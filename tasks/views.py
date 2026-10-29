from django.shortcuts import get_object_or_404, redirect, render

from .forms import TaskForm
from .models import Task


def home(request):
    tasks = Task.objects.all()
    form = TaskForm()
    return render(request, 'tasks/home.html', {'tasks': tasks, 'form': form})


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('home')


def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})


def toggle_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.toggle()
    return redirect('home')


def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('home')
