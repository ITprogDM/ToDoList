from django.urls import path
from .views import *

urlpatterns = [
    path('todoapp/', index, name='index'),
    path('addTodoItem/', AddToDo, name='AddToDo'),
    path('deleteTodoItem/<int:i>/', deleteTodoView),
]