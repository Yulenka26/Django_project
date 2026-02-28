from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from slugify import slugify
from rest_framework import generics, viewsets, permissions

from project.blog_app.models import Post, Category
from project.drf_api.permissions import IsAuthorOrReadOnly
from project.drf_api.serializers import PostSerializer, CategorySerializer, FeedbackSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    )
    filterset_fields = ["category", "published"]
    search_fields = ["title", "content"]
    ordering_fields = ["created_at"]

    def perform_create(self, serializer):
        title = serializer.validated_data["title"]
        slug = slugify(title)
        serializer.save(author=self.request.user, slug=slug)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    )
    filterset_fields = ["title"]
    search_fields = ["title"]
    ordering_fields = ["title"]

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

    def perform_create(self, serializer):
        title = serializer.validated_data["title"]
        slug = slugify(title)
        serializer.save(slug=slug)

class FeedbackCreateAPIView(generics.CreateAPIView):
    serializer_class = FeedbackSerializer
