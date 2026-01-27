from project.blog_app.models import Post, Category
from django.shortcuts import get_object_or_404, render


def index(request):
    posts = Post.objects.filter(published=True).order_by("-created_at")[:5]

    context = {
        "posts": posts
    }
    return render(request, 'blog_app/index.html', context=context)

def post_list(request):
    posts = Post.objects.filter(published=True).order_by("-created_at")

    context = {
        "posts": posts
    }
    return render(request, 'blog_app/post_list.html', context=context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    context = {
        "post": post
    }
    return render(request, 'blog_app/post_detail.html', context=context)

def categories_list(request):
    categories = Category.objects.all()

    context = {
        "categories": categories
    }
    return render(request, 'blog_app/categories_list.html', context=context)

def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    posts = Post.objects.filter(category=category, published=True).order_by("-created_at")

    context = {
        "category": category,
        "posts": posts
    }
    return render(request, 'blog_app/category_detail.html', context=context)
