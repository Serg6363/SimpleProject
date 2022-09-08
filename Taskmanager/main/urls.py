from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('make', views.make_task, name='make'),
    path('appointment', views.all_appointments, name='appoi'),
]
