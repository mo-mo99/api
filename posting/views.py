from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import PostSerializer
from .models import *


@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'post by subject':'/post-by-sub/<str:pk>/',
        'delete': '/delete-post/<str:pk>/',
        'update':'/update-post/<str:pk>/',
        'create':'/create-post/',
        'post by user':'/post-by-user/<str:pk>/'
    }
    return Response(api_urls)

@api_view(['GET'])
def postList(request, pk):
    posts = Post.objects.all()
    currents = posts.filter(subject_id= pk)
    serializer = PostSerializer(currents, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_post(request):
    serializer = PostSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def update_post(request, pk):
    post = Post.objects.get(id = pk)
    serializer = PostSerializer(instance=post, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    
    return Response('item deleted')

@api_view(['GET'])
def user_posts(request):
    user_id = request.user.id
    posts = [i for i in Post.objects.all() if i.owner_id == user_id]
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)