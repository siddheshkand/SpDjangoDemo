from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Todo
# Create your views here.


def hello_world(request):

    # return HttpResponse('Hello World')
    c = 2 + 3
    
    return render(
        request,
        'todo/todo.html',
        {
            "todo": Todo.objects.all(),
            "numbers": [45, 43, 56],
            "high_computation":c,
            
        }
    )

def is_admin(request):
    is_admin = True
    return render(
        request,
        'todo/is_admin.html',
        {
            "is_admin":is_admin
        }
    )