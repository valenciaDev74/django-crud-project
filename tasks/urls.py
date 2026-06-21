from django.urls import path
from . import views

urlpatterns = [
    path("", views.tasks, name="tasks"),
    path("<int:task_id>/", views.task_detail, name="task_detail"),
    path("create/", views.create_task, name="create_task"),
    path("<int:task_id>/complete/", views.task_completed, name="task_completed"),
    path("<int:task_id>/delete/", views.delete_task, name="delete_task"),
    path("completed/", views.tasks_completed, name="tasks_completed"),
]
