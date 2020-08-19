from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ToDo
from .forms import ToDoForm


def toDoApp(request):
    form = ToDoForm()
    if request.method == "POST":
        form = ToDoForm(request.POST or None)
        if form.is_valid():
            form.save()

    todos = ToDo.objects.all().order_by('-id')
    return render(request, 'pages/index.html', {"todos": todos, "form": form})

def deleteToDo(request, id):
    affectedToDo = ToDo.objects.get(id=id)
    affectedToDo.delete()
    return HttpResponseRedirect('/')

def aboutPage(request):
    return render(request, 'pages/about.html')


