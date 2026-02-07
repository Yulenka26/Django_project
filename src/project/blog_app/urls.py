from django.urls import path
from project.blog_app import views


app_name = "blog"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path("post_list/", views.PostListView.as_view(), name='post_list'),
    path("post/<slug:slug>/edit/", views.edit_post, name='edit_post'),
    path("post/<slug:slug>/", views.PostDetailView.as_view(), name='post_detail'),
    path("categories/", views.categories_list, name='categories_list'),
    path("categories/<int:category_id>/", views.category_detail, name='category_detail'),
    path("create_post/", views.post_create, name='create_post'),
    path("category/create/", views.CategoryCreateView.as_view(), name='create_category'),
]
