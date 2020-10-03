from django.urls import reverse_lazy
from django.views import generic
from todo.models import Todo
from django.shortcuts import render, get_object_or_404
from datetime import date
from django.http import  HttpResponseRedirect
from todo.forms import TodoForm



# filter(added_date=today)

def index(request):
      today = date.today()
      todos = Todo.objects.filter(added_date=date.today())
      totaltime = sum([t.time for t in todos])
      context = {
        'todos': todos,
        'today': today,
        'totaltime': totaltime,

        }
      return render(request, 'todo/index.html',context)

def addTodo(request):
      new_todo = Todo(title=request.POST['title'],added_date = request.POST['added_date'],text=request.POST['text'],time=request.POST['time'],importance=request.POST['importance'])
      new_todo.save()
      return HttpResponseRedirect('/todo/')

def delete(request,id):
    todo = get_object_or_404(Todo, pk=id)
    todo.delete()
    return HttpResponseRedirect('/todo/')

def edit(request,id):
    todo = get_object_or_404(Todo, pk=id)
    todoForm = TodoForm(instance=todo)
    context = {
        'message': 'Edit Article',
        'todo': todo,
        'todoForm': todoForm,
    }
    return render(request, 'todo/edit.html' ,context)

def update(request, id):
    if request.method == 'POST':
        todo = get_object_or_404(Todo, pk=id)
        todoForm = TodoForm(request.POST,instance=todo)
        if todoForm.is_valid():
            todoForm.save()

    context = {
        'message': 'Update article ' + str(id),
        'todo': todo,
    }
    return HttpResponseRedirect('/todo/',context)

class DetailView(generic.DetailView):
       model = Todo

