from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class CKAdmin(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)
    subscription = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Post
        fields = "__all__"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    form = CKAdmin
    list_display = ('title', 'slug', 'created_at', 'category', 'get_photo', "views")
    list_filter = ('category', "created_at")
    readonly_fields = ('created_at', 'get_photo')
    fields = ('title', 'slug', 'content', 'subscription', 'category', 'photo', 'get_photo', 'created_at', 'views', 'tags')
    save_as = True
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f"<img class='' src = '{obj.photo.url}'width = '50'>")
        return "None"
    get_photo.short_description = "Миниатюра"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Similar)
class SimilarAdmin(admin.ModelAdmin):
    list_display = ("title", "subscriptions", "get_photo")

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f"<img src = '{obj.photo.url}'width = '50'>")
        return "None"
    get_photo.short_description = "Миниатюра"


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "message", "email", "website", "create_at")
