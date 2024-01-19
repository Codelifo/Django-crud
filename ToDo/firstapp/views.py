from django.shortcuts import render, redirect
from .forms import ToDoForm
from .models import ToDoModel
# Create your views here.

def Home(request):
    return render(request, 'base.html')

def creat_target(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_tar')
    else:
        form = ToDoForm()
    return render(request, 'creat_todo.html', {'form':form})

def showtarget(request):
    ToDo = ToDoModel.objects.all()
    return render(request, 'show_target.html', {'data':ToDo})

def edit_ToDo(request, id):
    ToDo = ToDoModel.objects.get(pk = id)
    form = ToDoForm(instance=ToDo)
    if request.method == 'POST':
        form = ToDoForm(request.POST,instance= ToDo)
        if form.is_valid():
            form.save()
            return redirect('show_tar')     
    return render(request, 'creat_todo.html', {'form':form})

def Delete(request, id):
    ToDo = ToDoModel.objects.get(pk = id).delete()
    return redirect('show_tar')