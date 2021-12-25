from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('posts', views.PostViewSet)
router.register('tags', views.TagsViewSet)


urlpatterns = [
    path("categories/", views.CategoriesListView.as_view()),
    path("category/add", views.CreateCategoryView.as_view()),
]

urlpatterns += router.urls






