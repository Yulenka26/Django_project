from rest_framework import serializers

from project.blog_app.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "title", "slug", "content", "author", "published", "created_at", "category")
