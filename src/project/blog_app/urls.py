from django.urls import path
from project.blog_app import views


app_name = "blog"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path("post_list/", views.PostListView.as_view(), name='post_list'),
    path("post/<slug:slug>/edit/", views.PostUpdateView.as_view(), name='edit_post'),
    path("post/<slug:slug>/", views.PostDetailView.as_view(), name='post_detail'),
    path("categories/", views.CategoriesListView.as_view(), name='categories_list'),
    path("categories/<int:category_id>/", views.CategoryDetailView.as_view(), name='category_detail'),
    path("create_post/", views.PostCreateView.as_view(), name='create_post'),
    path("category/create/", views.CategoryCreateView.as_view(), name='create_category'),
]
