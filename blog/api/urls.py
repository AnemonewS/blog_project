from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from blog.api import api

post_create = api.CreatePostViewSet.as_view({
    'post': 'create',
    'get': 'list',
})


urlpatterns = format_suffix_patterns([
    path("post/", views.PostListViewSet.as_view({"get": "list"})),
    path("post/<int:pk>/", views.PostListViewSet.as_view({"get": "retrieve"})),
    path("post/add/", post_create, name="post_create"),
    path("tags/add/", views.CreateTagsView.as_view()),
    path("categories/", views.CategoriesListView.as_view()),
    path("tags/", views.TagsListView.as_view()),
    path("category/add", views.CreateCategoryView.as_view()),

    path("post-view/", api.PostViewSet.as_view({'get': 'list'})),
    path("post-view/<int:pk>/", api.PostViewSet.as_view({'get': 'retrieve'})),
])

router = DefaultRouter()




