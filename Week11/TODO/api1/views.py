from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from main.models import Task

@csrf_exempt
def task_list(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        for task in tasks:
            task.to_json()
        return JsonResponse(Task.objects.first().to_json(), safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        tlist = Task(
            name=data['name'], 
            created=data['created'], 
            due_on=data['due_on'], 
            owner=data['owner'], 
            mark=data['mark']
        )
        tlist.save()
        return JsonResponse(tlist.to_json())

@csrf_exempt
def task_detail(request, pk):
    try:
        task = Task.objects.get(id=pk)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=404)

    if request.method == 'GET':
        return JsonResponse(task.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        task.name = data.get('name', task.name)
        task.created = data.get('created', task.created)
        task.due_on = data.get('due_on', task.due_on)
        task.mark = data.get('mark', task.mark)
        task.save()
        return JsonResponse(task.to_json())
    elif request.method == 'DELETE':
        task.delete()
        return JsonResponse({'deleted': True}, status=204)