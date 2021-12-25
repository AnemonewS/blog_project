from django.db import models
from django.urls import reverse

"""
    Post
    =============
    title, slug, photo, archives, created_at, content, comments, tags, category, 
    
    Tag
    =============
    title, slug 
    
    Category
    =============
    title, slug
"""


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name="Имя")
    slug = models.SlugField(max_length=150, verbose_name="URL", unique=True, null=True)

    def get_absolute_url(self):
        return reverse("category", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["title"]


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    slug = models.SlugField(max_length=150, verbose_name="URL", null=True)
    photo = models.ImageField(upload_to="photo/",verbose_name="Фото", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Публикация")
    content = models.TextField(verbose_name="Содержание", blank=True)
    comments = models.TextField(verbose_name="Комментарии", blank=True)
    subscription = models.TextField(verbose_name="Описание", blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категории", null=True, blank=True, related_name="post")
    views = models.IntegerField(default=0, verbose_name="Просмотры")

    def get_absolute_url(self):
        return reverse("post", kwargs={"views_id": self.id})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["created_at"]


class Similar(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    photo = models.ImageField(upload_to="similar_photo/", verbose_name="Обложка")
    subscriptions = models.TextField(verbose_name="Описание")
    artist = models.CharField(max_length=150, verbose_name="Имя")
    slug = models.SlugField(max_length=69, verbose_name="URL", unique=True, null=True)

    def get_absolute_url(self):
        return reverse("similar", kwargs={"similar_id": self.id})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Похожий"
        verbose_name_plural = "Похожие"
        ordering = ["id"]
