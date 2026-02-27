from rest_framework import generics

from project.blog_app.models import Post, Category
from project.drf_api.serializers import PostSerializer, CategorySerializer, FeedbackSerializer


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.filter(published=True)
    serializer_class = PostSerializer

class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class FeedbackCreateAPIView(generics.CreateAPIView):
    serializer_class = FeedbackSerializer
