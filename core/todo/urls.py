from django.urls import path
from .views import update_task,delete_task, done_task, home_view

app_name = 'todo'

urlpatterns = [
    path('', home_view, name="task_list"),
    path('update/<int:pk>/', update_task, name="update_task"),
    path('delete/<int:pk>/', delete_task, name="delete_task"),
    path('done/<int:pk>/', done_task, name="done_task"),
]

