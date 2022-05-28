from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Todo
# Create your views here.
from todo.forms import MySampleForm, MyTodoForm


def hello_world(request):

    my_form={}
    if request.method == 'POST':
        print("Post Called")
        my_form = MySampleForm(request.POST)
        # check whether it's valid:
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Todo.objects.create(
                title=my_form.cleaned_data["title"],
                description=my_form.cleaned_data["description"],

            )
            my_form = MySampleForm()
    else:
        print("Get Called")
        my_form = MySampleForm()
    # c = 2 + 3

    return render(
        request,
        'todo/todo.html',
        {
            "todo": Todo.objects.all(),
            "numbers": [45, 43, 56],
            # "high_computation": c,
            "my_custom_form": my_form
        }
    )


def is_admin(request):
    is_admin = True
    return render(
        request,
        'todo/is_admin.html',
        {
            "is_admin": is_admin,
            "my_custom_form": MySampleForm
        }
    )


def django_model_form(request):
    my_form ={}
    if request.method == 'POST':
    
        my_form = MyTodoForm(request.POST)
        # check whether it's valid:
        if my_form.is_valid():
            my_form.save()
            my_form = MyTodoForm()
    else:
        my_form = MyTodoForm()
    
    return render(
        request,
        'todo/todo.html',
        {
            "todo": Todo.objects.all(),
            "numbers": [45, 43, 56],
            # "high_computation": c,
            "my_custom_form": my_form
        }
    )