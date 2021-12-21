from rest_framework import serializers
from blog.models import *
from django.utils.html import strip_tags


class PostSerializer(serializers.ModelSerializer):

    category = serializers.SlugRelatedField(slug_field="title", read_only=True)
    tags = serializers.SlugRelatedField(slug_field="title", read_only=True, many=True)

    class Meta:
        model = Post
        fields = ("id", "title", "category", "tags",)


class PostDetailSerializer(serializers.ModelSerializer):

    category = serializers.SlugRelatedField(slug_field="title", read_only=True)
    tags = serializers.SlugRelatedField(slug_field="title", read_only=True, many=True)

    class Meta:
        model = Post
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["content"] = strip_tags(instance.content)
        return data


class CreatePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"


class CreateTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = "__all__"


class CategoriesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ("title","slug")


class TagsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = "__all__"


class CreateCategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"
