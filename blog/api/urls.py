from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from blog.api import api


urlpatterns = format_suffix_patterns([
    path("post/", views.PostListView.as_view()),
    path("post/<int:pk>/", views.PostDetailView.as_view()),
    path("post/add/", views.CreatePostView.as_view()),
    path("tags/add/", views.CreateTagsView.as_view()),
    path("categories/", views.CategoriesListView.as_view()),
    path("tags/", views.TagsListView.as_view()),
    path("category/add", views.CreateCategoryView.as_view()),

    path("post-view/", api.PostViewSet.as_view({'get': 'list'})),
    path("post-view/<int:pk>/", api.PostViewSet.as_view({'get': 'retrieve'})),
])

# router = DefaultRouter()
#
# router.register(r'tags-read', api.TagsReadOnly, basename='tags')
# urlpatterns = router.urls


