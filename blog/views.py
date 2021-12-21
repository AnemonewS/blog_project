from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import UserRegisterForm, LoginForm
from .forms import AddNews


# class AddNewsForm(CreateView):
#     template_name = "blog/add_news_form.html"
#     form_class = AddNews
#     raise_exception = True

def add_news_form(request):
    if request.method == "POST":
        form = AddNews(request.POST)
        if form.is_valid():
            post = Post.objects.create(**form.cleaned_data)
            return redirect(post)
    else:
        form = AddNews()
    return render(request, "Portfolio/add_news_form.html", {"form": form})


# Registration
def registerform(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Успешная регистрация!")
            return redirect("home")
        else:
            messages.error(request, "Произошла непредвиденная ошибка!")

    else:
        form = UserRegisterForm()
    return render(request,"Portfolio/registration_form.html",{"form":form})


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


# class SimilarView(ListView):
#     model = Similar
#     template_name = "Portfolio/similar_post.html"
#     context_object_name = "similar"
#
#     def get_queryset(self):
#         return Similar.objects.select_related("category").filter(title__slug=self.kwargs["slug"])

def similar_post(request, similar_id):
    similar = Similar.objects.get(id=similar_id)
    return render(request, "Portfolio/similar_post.html", {"similar":similar})


def view_post(request, views_id):
    post = Post.objects.select_related("category").get(id=views_id)
    return render(request, "Portfolio/view_post.html", {"post": post})


# class ViewBlog(DetailView):  # Наша отдельная категория
#     model = Post
#     template_name = "blog/view_category.html"
#     context_object_name = "view"


class GetCategoryView(ListView):
    template_name = "Portfolio/category_get.html"
    context_object_name = "category_get"
    paginate_by = 3
    allow_empty = False

    def get_queryset(self):
        return Post.objects.select_related("category").filter(category__slug=self.kwargs["slug"])


class GetTagView(ListView):
    template_name = "Portfolio/home_page.html"
    context_object_name = "main_page"
    paginate_by = 2

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs["slug"])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(id=self.kwargs['categories_id'])
        return context


class SearchField(ListView):
    template_name = '_inc/_search_field.html'
    context_object_name = 'results'
    paginate_by = 2

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = f's = {self.request.GET.get("s")}'
        return context


def get_info(request):
    post = Post.objects.all()

    return render(request, 'Portfolio/get_info.html', {"post": post})

# def get_category(request,slug):
#     return render(request,'blog/category_get.html')


# def get_tag(request, slug):
#     return render(request, '_inc/_tag.html')
