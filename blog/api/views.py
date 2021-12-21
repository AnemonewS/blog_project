import django_filters
from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Post
from django_filters.rest_framework import DjangoFilterBackend
from .service import PostFilter
from .service import PaginationPost
from rest_framework.decorators import action

from .serializers import *


# Class with general info APIView
class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


# Class with detail info APIView
class PostDetailView(APIView):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)
#
#

# Class with create of Post APIView
class CreatePostView(APIView):
    def post(self, request):
        post = CreatePostSerializer(data=request.data)
        if post.is_valid():
            post.save()
            return Response(status=201)
        else:
            return Response(status=400)


# class PostListView(generics.ListAPIView):
#     serializer_class = PostSerializer
#     # filter_backends = (DjangoFilterBackend,)
#     filterset_class = PostFilter
#     filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
#     pagination_class = PaginationPost
#
#     def get_queryset(self):
#         posts = Post.objects.all()
#         return posts




# class PostViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Post.objects.all()
#
#     filterset_class = PostFilter
#     filter_backends = [django_filters.rest_framework.DjangoFilterBackend
#
#     def get_serializer_class(self):
#         if self.action == "list":
#             return PostSerializer
#         elif self.action == "retrieve":
#             return PostDetailSerializer


# class PostDetailView(generics.RetrieveAPIView):
#
#     queryset = Post.objects.all()
#     serializer_class = PostDetailSerializer
#
#
# class CreatePostView(generics.CreateAPIView):
#
#     serializer_class = CreatePostSerializer


class CreateTagsView(generics.CreateAPIView):

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

    serializer_class = CreateCategoriesSerializer

