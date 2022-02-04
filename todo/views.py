from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
# Create your views here.
@login_required
def current(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request,'todo/current.html',{'todos':todos})
@login_required
def create(request):
    if request.method =='GET':
        return render(request,'todo/create.html',{'form':TodoForm()})
    else:
        form = TodoForm(request.POST)
        newtodo = form.save(commit=False)
        newtodo.user = request.user
        newtodo.save()
        return redirect('current')

def inspecttodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        return render(request,'todo/inspecttodo.html',{'todo':todo,'form':form})
    else:
            form = TodoForm(request.POST,instance=todo)
            form.save()
            return redirect("current")

def deletetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':

        todo.delete()
        return redirect('current')

def completetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == "POST":
        todo.datecompleted = timezone.now()
        todo.save()
        return redirect('current')

def displaycompleted(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=False)
    return render(request,'todo/displaycompleted.html',{'todos':todos})
