from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from main.models import Task
from .serializers import TaskModelSerializer, UserModelSerializer
from django.http import Http404
from django.contrib.auth.models import User

class TaskView(APIView):
    def get(self, request):
        posts = Task.objects.all()
        serializer = TaskModelSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class TaskDetailView(APIView):
    def get_object(self, pk):
        try:
            return Task.objects.get(id=pk)
        except Task.DoesNotExist:
            return Http404

    def get(self, request, pk):
        post = Task.objects.get(id=pk)
        serializer = TaskModelSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = Task.objects.get(id=pk)
        serializer = TaskModelSerializer(instance=post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = Task.objects.get(id=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TaskGenView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

class TaskDetailGenView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer

    def get_object(self):
        return Task.objects.get(id=self.kwargs['pk'])

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is None:
        return Response({'error': 'Invalid data'})
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})

@api_view(['GET'])
def logout(request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def register(request):
    serialized = UserModelSerializer(data=request.data)
    if serialized.is_valid():
        User.objects.create_user(
            request.data.get('username'),
            request.data.get('email'),
            request.data.get('password')
        )
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

