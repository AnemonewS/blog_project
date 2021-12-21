from django_filters import rest_framework as filters
from rest_framework.response import Response

from blog.models import Post
from rest_framework.pagination import PageNumberPagination


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class PostFilter(filters.FilterSet):

    category = CharFilterInFilter(field_name="category__title", lookup_expr="in")
    tags = CharFilterInFilter(field_name="tags__title", lookup_expr="in")

    class Meta:
        model = Post
        fields = ("category", "tags")


class PaginationPost(PageNumberPagination):
    page_size = 2
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response({
            'links':
                self.get_next_link()
        })





