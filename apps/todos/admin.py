from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'status', 'due_date', 'user']
    list_filter = ['status', 'due_date', 'user']

admin.site.register(Todo, TodoAdmin)
