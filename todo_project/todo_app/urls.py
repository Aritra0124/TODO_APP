from django.urls import path

from . import views

urlpatterns = [
    path('', views.login_page, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.signout, name='logout'),
    path('project/', views.project_response, name='project'),
    path('task/', views.task_response, name='task'),
    path('get_sections/', views.get_section_names, name='get_sections'),
    path('create_task/', views.create_task, name='create_task'),
    path('edit_task/', views.edit_task, name='edit_task'),
    path('delete_task/', views.task_delete, name='delete_task'),
]