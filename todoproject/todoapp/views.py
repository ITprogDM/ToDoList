from django.shortcuts import render
from .models import ToDoListItem
from django.http import HttpResponseRedirect

def index(request):
    all_todo_items = ToDoListItem.objects.all()
    context = {
        'all_items':all_todo_items
    }
    return render(request, 'todolist.html', context)

def AddToDo(request):
    r = request.POST['content']
    new_item =ToDoListItem(content = r)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')

def deleteTodoView(request):
    y = ToDoListItem.objects.get(id=1)
    y.delete()
    return HttpResponseRedirect('/todoapp/')