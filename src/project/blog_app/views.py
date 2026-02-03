from project.blog_app.forms import PostForm, SearchForm, CategoryForm
from project.blog_app.models import Post, Category
from django.shortcuts import get_object_or_404, render, redirect
from slugify import slugify


def index(request):
    posts = Post.objects.filter(published=True).order_by("-created_at")

    form = SearchForm(request.GET)

    if form.is_valid():
        query = form.cleaned_data["query"].strip()
        if query:
            posts = posts.filter(title__icontains=query)

    context = {
        "posts": posts,
        "form": form
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

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.slug = slugify(new_post.title)
            new_post.save()

            return redirect("blog:post_detail", new_post.slug)
    else:
        form = PostForm()

    context = {
        "form": form,
        "title": "Добавление статьи",
        "button_text": "Добавить"
    }
    return render(request, "blog_app/create_post.html", context=context)

def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            new_category = form.save(commit=False)
            new_category.save()

            return redirect("blog:categories_list")
    else:
        form = CategoryForm()

    context = {
        "form": form
    }
    return render(request, "blog_app/create_post.html", context=context)

def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            edited_post = form.save(commit=False)
            edited_post.slug = slugify(edited_post.title)
            edited_post.save()
            return redirect("blog:post_detail", edited_post.slug)
    else:
        form = PostForm(instance=post)

    context = {
        "form": form,
        "title": "Редактирование статьи",
        "button_text": "Сохранить"
    }

    return render(request, "blog_app/create_post.html", context=context)
