from django.urls import path, include
from .views import *


urlpatterns = [
    # Register, login, logout forms
    path('register/', registerform,name = "register"),
    path('loginForm/', loginForm, name="loginForm"),
    path('logoutForm/', logoutform, name="logoutForm"),

    path('similar_post/<int:similar_id>/', similar_post, name="similar"),

    # Function forms
    path('add_news/', add_news_form, name="add_news"),
    path('post/<int:views_id>/', view_post, name='post'),
    path("get_info/", get_info, name="get_info"),

    # Class forms
    path('', HomePageView.as_view(), name="home"),
    # path('view_news/<str:slug>', ViewBlog.as_view(), name="view_news"),
    path('category/<str:slug>/', GetCategoryView.as_view(), name="category"),

    path('tag/<str:slug>', GetTagView.as_view(), name="tag"),
    path('search/', SearchField.as_view(), name="search"),


    # path("api/", include("blog.api.urls")),

]