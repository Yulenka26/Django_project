from django.urls import path
from . import views


app_name = "blog"
urlpatterns = [
    path('', views.index, name='index'),
    path("post_list/", views.post_list, name='post_list'),
    path("post/<int:post_id>/", views.post_detail, name='post_detail'),
]
