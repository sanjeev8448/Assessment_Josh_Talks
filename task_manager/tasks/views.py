from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task, User
from .serializers import TaskSerializer, TaskCreateSerializer, UserSerializer

# API to create a task
class TaskCreateAPIView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer

class TaskAssignAPIView(APIView):
    def post(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
            user_ids = request.data.get("assigned_users", [])
            users = User.objects.filter(id__in=user_ids)

            if not users.exists():
                return Response({"error": "No valid users found"}, status=status.HTTP_400_BAD_REQUEST)

            task.assigned_users.set(users)
            task.save()

            # ✅ Serialize assigned users
            assigned_users_data = UserSerializer(users, many=True).data

            return Response({
                "message": "Task assigned successfully",
                "task_id": task.id,
                "assigned_users": assigned_users_data  # ✅ Corrected this line
            }, status=status.HTTP_200_OK)

        except Task.DoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)


# API to get tasks assigned to a specific user
class UserTasksAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        return Task.objects.filter(assigned_users__id=user_id)
