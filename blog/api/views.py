import django_filters
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .serializers import *

class PostListViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)


class CreateTagsView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

    serializer_class = CreateTagSerializer


class CategoriesListView(generics.ListAPIView):

    serializer_class = CategoriesListSerializer

    def get_queryset(self):
        categories = Category.objects.all()
        return categories


class TagsListView(generics.ListAPIView):

    serializer_class = TagsListSerializer

    def get_queryset(self):
        tags = Tag.objects.all()
        return tags


class CreateCategoryView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateCategoriesSerializer

