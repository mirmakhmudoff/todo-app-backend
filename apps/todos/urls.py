from django.urls import path
from .views import TodoListCreateView, TodoStatusUpdateView, TodoDeleteView

urlpatterns = [
    path('', TodoListCreateView.as_view(), name='todo-list-create'),
    path('<int:pk>/status/', TodoStatusUpdateView.as_view(), name='todo-status-update'),
    path('<int:pk>/delete/', TodoDeleteView.as_view(), name='todo-delete'),
]
