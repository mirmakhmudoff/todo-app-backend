from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Todo
from .serializers import TodoSerializer, TodoStatusUpdateSerializer
from django.utils import timezone
from datetime import timedelta

class TodoListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        filter_type = request.query_params.get('filter', None)
        today = timezone.now().date()
        todos = Todo.objects.filter(user=request.user)
        
        if filter_type == 'daily':
            todos = todos.filter(due_date=today)
        elif filter_type == 'weekly':
            start_week = today - timedelta(days=today.weekday())
            end_week = start_week + timedelta(days=6)
            todos = todos.filter(due_date__range=[start_week, end_week])
        elif filter_type == 'monthly':
            todos = todos.filter(due_date__month=today.month)

        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoStatusUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk, user=request.user)
        except Todo.DoesNotExist:
            return Response({"error": "Todo not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TodoStatusUpdateSerializer(data=request.data)
        if serializer.is_valid():
            todo.status = serializer.validated_data["status"]
            todo.save()
            todo_serializer = TodoSerializer(todo)
            return Response(todo_serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

