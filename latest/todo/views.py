from django.shortcuts import render, get_object_or_404, redirect
from .models import TodoItem
from .forms import TodoItemForm

def index(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo:index')
    else:
        form = TodoItemForm()
    return render(request, 'todo/add_todo.html', {'form': form})

def edit_todo(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    if request.method == 'POST':
        form = TodoItemForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo:index')
    else:
        form = TodoItemForm(instance=todo)
    return render(request, 'todo/edit_todo.html', {'form': form})

def delete_todo(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo:index')
    return render(request, 'todo/delete_todo.html', {'todo': todo})
