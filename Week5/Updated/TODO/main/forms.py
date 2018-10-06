from django.forms import ModelForm
from main.models import Task,Owner

class TaskCreate(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'created', 'due_on', 'owner', 'mark'] 