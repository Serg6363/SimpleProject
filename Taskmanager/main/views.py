from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def make_task(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена не верно'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/make_task.html', context)


def all_appointments(request):
    return render(request, 'main/appointments.html')
