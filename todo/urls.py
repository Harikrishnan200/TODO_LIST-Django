from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('add_task', views.add_task,name='add_task'),
    path('delete_task/<int:pk>', views.delete_task,name='delete_task'),
    path('edit_task/<int:pk>', views.edit_task,name='edit_task'),
    path('change_status/<int:pk>', views.change_status,name='change_status'),
    path('login', views.login,name='login'),
]