from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Todo
# Create your views here.

def hello_world(request):
    
    # return HttpResponse('Hello World')
    return render(request,'todo/todo.html' , {"todo": Todo.objects.all(),"numbers" :[45,43,56]})