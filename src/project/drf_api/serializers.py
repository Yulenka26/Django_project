from rest_framework import serializers

from project.blog_app.models import Post, Category
from project.feedback_app.models import one_choice, Feedback


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "title", "slug", "content", "author", "published", "created_at", "category")

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "title", "slug")

class FeedbackSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    subject = serializers.ChoiceField(choices=one_choice)
    message = serializers.CharField()

    def create(self, validated_data):
        return Feedback.objects.create(**validated_data)
