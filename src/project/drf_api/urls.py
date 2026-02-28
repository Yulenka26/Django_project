from django.urls import path, include
from rest_framework.routers import DefaultRouter

from project.drf_api.views import CategoryListCreateAPIView, \
    CategoryRetrieveUpdateDestroyAPIView, FeedbackCreateAPIView, PostViewSet

app_name = "drf_api"

router = DefaultRouter()
router.register("posts", PostViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("categories/", CategoryListCreateAPIView.as_view(), name="category_list_create"),
    path("categories/<int:pk>/", CategoryRetrieveUpdateDestroyAPIView.as_view(), name="Category_detail"),
    path("feedback/", FeedbackCreateAPIView.as_view(), name="feedback_create"),
]
