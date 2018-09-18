from django.shortcuts import render

def current_tasks(request):
    tasks = [
        {
        'name': 'Task 1',
        'created': '18/09/18',
        'due_on': '26/09/18',
        'owner': 'Yeldan',
        'mark': True
        },
        {
        'name': 'Task 2',
        'created': '18/09/18',
        'due_on': '26/09/18',
        'owner': 'Yeldan',
        'mark': True
        },
        {
        'name': 'Task 3',
        'created': '18/09/18',
        'due_on': '26/09/18',
        'owner': 'Yeldan',
        'mark': True
        }
    ]

    context = { 'tasks': tasks }

    return render(request, 'todo_list.html', context)

def finished_tasks(request):
	tasks = [
        {
        'name': 'Task 4',
	    'created': '18/09/18',
	    'due_on': '23/09/18',
	    'owner': 'Yeldan',
        'mark': False
        }
    ]

	context = { 'tasks': tasks }

	return render(request, 'completed_todo_list.html', context)