from django.urls import path
from .views import TodoListCreateView, TodoStatusUpdateView

urlpatterns = [
    path('', TodoListCreateView.as_view(), name='todo-list-create'),
    path('<int:pk>/status/', TodoStatusUpdateView.as_view(), name='todo-status-update'),
]
