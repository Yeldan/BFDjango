from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from main.models import Post

@csrf_exempt
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        for post in posts:
            post.to_json()
        return JsonResponse(Post.objects.first().to_json(), safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        plist = Post(
            title=data['title'],
            author=data['author'],
            date_published=data['date_published'],
            content=data['content'],
            comment=data['comment'],
        )
        plist.save()
        return JsonResponse(plist.to_json())

@csrf_exempt
def post_detail(request, pk):
    try:
        post = Post.objects.get(id=pk)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=404)

    if request.method == 'GET':
        return JsonResponse(post.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        post.title = data.get('title', post.title)
        post.author = data.get('author', post.author)
        post.date_published = data.get('date_published', post.date_published)
        post.content = data.get('content', post.content)
        post.comment = data.get('comment', post.comment)
        post.save()
        return JsonResponse(post.to_json())
    elif request.method == 'DELETE':
        post.delete()
        return JsonResponse({'deleted': True}, status=204)