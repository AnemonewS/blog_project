from django.urls import path, include
from .views import *


urlpatterns = [
    # Register, login, logout forms
    path('register/', RegisterView.as_view(), name="register"),
    path('loginForm/', loginForm, name="loginForm"),
    path('logoutForm/', logoutform, name="logoutForm"),

    path('recent-post/<int:recent_id>/', recent_post, name="recent"),

    # Function forms
    path('add-news/', AddNewsView.as_view(), name="add_news"),
    path('post/<int:views_id>/', view_post, name='post'),
    path('tags/<str:slug>/', GetTagsView.as_view(), name='tags'),
    path("feedback/", FeedbackView.as_view(), name="feedback"),

    # Class forms
    path('', HomePageView.as_view(), name="home"),
    path('category/<str:slug>/', GetCategoryView.as_view(), name="category"),

    path('search/', SearchFieldView.as_view(), name="search"),
]
