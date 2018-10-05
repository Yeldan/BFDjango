from django.contrib import admin
from .models import Owner, Task

class CustomOwner(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    list_per_page = 3

class CustomTask(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'due_on', 'owner', 'mark')
    list_display_links = ('id', 'name', 'created', 'due_on', 'owner', 'mark')
    search_fields = ('id', 'name', 'created', 'due_on')
    list_per_page = 5

admin.site.register(Owner, CustomOwner)
admin.site.register(Task, CustomTask)
