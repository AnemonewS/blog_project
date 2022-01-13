from rest_framework import generics, permissions, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from .serializers import *


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return [AllowAny()]
        return super(PostViewSet, self).get_permissions()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PostDetailSerializer
        return super(PostViewSet, self).get_serializer_class()


class CategoriesListView(generics.ListAPIView):

    serializer_class = CategoriesSerializer

    def get_queryset(self):
        categories = Category.objects.all()
        return categories


class CreateCategoryView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = CreateCategoriesSerializer
