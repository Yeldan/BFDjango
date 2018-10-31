from django.contrib import admin
from .models import Task

class CustomTask(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'due_on', 'owner', 'mark')
    list_display_links = ('id', 'name', 'created', 'due_on', 'owner', 'mark')
    search_fields = ('id', 'name', 'created', 'due_on')
    list_per_page = 10

admin.site.register(Task, CustomTask)
