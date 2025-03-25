from django.urls import path
from .views import TaskCreateAPIView, TaskAssignAPIView, UserTasksAPIView

urlpatterns = [
    # Endpoint for creating a new task
    path('tasks/create/', TaskCreateAPIView.as_view(), name='task-create'),
    
    # Endpoint for assigning a task to one or more users
    path('tasks/<int:pk>/assign/', TaskAssignAPIView.as_view(), name='task-assign'),
    
    # Endpoint for retrieving all tasks assigned to a specific user
    path('users/<int:user_id>/tasks/', UserTasksAPIView.as_view(), name='user-tasks'),
]
