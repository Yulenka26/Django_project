from django.urls import path

from project.drf_api.views import PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView

app_name = "drf_api"
urlpatterns = [
    path("posts/", PostListCreateAPIView.as_view(), name="post_list_create"),
    path("posts/<int:pk>/", PostRetrieveUpdateDestroyAPIView.as_view(), name="post_detail"),
]
