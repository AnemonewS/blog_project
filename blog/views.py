from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth import login, logout
from .models import *
from .forms import UserRegisterForm, LoginForm, ContactForm, AddNewsForm


class AddNewsView(CreateView):
    template_name = "Portfolio/add_news.html"
    form_class = AddNewsForm
    context_object_name = "form"


class RegisterView(CreateView):
    template_name = "Portfolio/register_form.html"
    form_class = UserRegisterForm
    context_object_name = "form"
    success_url = reverse_lazy('login')


def loginForm(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = LoginForm()
    return render(request, "Portfolio/login_form.html", {"form": form})


def logoutform(request):
    logout(request)
    return redirect("home")


class HomePageView(ListView):  # Основная страница
    model = Post
    template_name = "Portfolio/home_page.html"
    context_object_name = "main_page"
    paginate_by = 2
    select_related = "category"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Главная страница"
        return context


class GetTagsView(ListView):
    model = Post
    template_name = 'Portfolio/tag_get.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs["slug"])


def recent_post(request, recent_id):
    recent = Similar.objects.get(id=recent_id)
    return render(request, "Portfolio/recent_post.html", {"recent": recent})


def view_post(request, views_id):
    post = Post.objects.select_related("category").get(id=views_id)
    return render(request, "Portfolio/view_post.html", {"post": post})


class GetCategoryView(ListView):
    template_name = "Portfolio/get_category.html"
    context_object_name = "category_get"
    paginate_by = 3
    allow_empty = False

    def get_queryset(self):
        return Post.objects.select_related("category").filter(category__slug=self.kwargs["slug"])


class SearchFieldView(ListView):
    template_name = '_inc/_search_field.html'
    context_object_name = 'results'
    paginate_by = 2

    def get_queryset(self):

        return Post.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = f's = {self.request.GET.get("s")}'
        return context


class FeedbackView(CreateView):
    form_class = ContactForm
    success_url = '/'
    template_name = 'Portfolio/feedback.html'

