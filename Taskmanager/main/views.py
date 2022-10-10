from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def make_task(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

            html_content = render_to_string(
                'main/task_created.html',
                {
                    'task': TaskForm,
                }
            )

            msg = EmailMultiAlternatives(
                subject=f'Новая запись: {form.cleaned_data["title"]}',
                body=form.cleaned_data['task'],
                from_email='mi5sing@yandex.ru',
                to=['sergei.dd11@gmail.com', ],
            )
            msg.attach_alternative(html_content, "text/html")

            msg.send()

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
