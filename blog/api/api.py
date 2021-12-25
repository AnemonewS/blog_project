from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from blog.models import Post, Tag
from .serializers import PostSerializer, PostDetailSerializer, TagsListSerializer, CreatePostSerializer


class PostViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)


class CreatePostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = CreatePostSerializer


class TagsReadOnly(viewsets.ViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagsListSerializer
    permission_classes = [IsAuthenticated]





