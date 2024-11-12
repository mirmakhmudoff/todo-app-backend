from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    due_date = serializers.DateField(required=True)

    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'status', 'due_date', 'created_at', 'updated_at']


class TodoStatusUpdateSerializer(serializers.Serializer):
    status = serializers.CharField(required=True, max_length=50)