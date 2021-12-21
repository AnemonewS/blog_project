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


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    form = CKAdmin
    list_display = ('title', 'slug', 'created_at', 'category', 'get_photo', "views")
    list_filter = ('category', "created_at")
    readonly_fields = ('created_at', 'get_photo')
    fields = ('title', 'slug', 'content', 'subscription', 'category', 'tags', 'photo', 'get_photo', 'created_at', 'views')
    save_as = True
    save_on_top = True

    # save_as_continue = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f"<img class='' src = '{obj.photo.url}'width = '50'>")
        return "None"
    get_photo.short_description = "Миниатюра"


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class SimilarAdmin(admin.ModelAdmin):
    list_display = ("title", "subscriptions", "get_photo")

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f"<img src = '{obj.photo.url}'width = '50'>")
        return "None"
    get_photo.short_description = "Миниатюра"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Similar, SimilarAdmin)