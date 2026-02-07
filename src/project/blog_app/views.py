from django.views.generic import TemplateView, ListView, DetailView, CreateView

from project.blog_app.forms import PostForm, CategoryForm
from project.blog_app.models import Post, Category
from django.shortcuts import get_object_or_404, render, redirect
from slugify import slugify

class IndexView(TemplateView):
    template_name = "blog_app/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.filter(published=True).order_by("-created_at")[:5]
        return context

class PostListView(ListView):
    model = Post
    template_name = "blog_app/post_list.html"
    context_object_name = "posts"
    paginate_by = 3

    def get_queryset(self):
        return self.model.objects.filter(published=True)


class PostDetailView(DetailView):
    model = Post
    template_name = "blog_app/post_detail.html"
    context_object_name = "post"

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

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "blog_app/create_category.html"

    def form_valid(self, form):
        form.instance.slug = slugify(form.cleaned_data["title"])
        return super().form_valid(form)


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
