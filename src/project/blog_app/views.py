from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)
from slugify import slugify

from project.blog_app.forms import CategoryForm, PostForm
from project.blog_app.mixins import StaffRequiredMixin, TitleMixin
from project.blog_app.models import Category, Post
from project.blog_app.tasks import increment_views_count


class IndexView(TitleMixin, TemplateView):
    template_name = "blog_app/index.html"
    title = "Главная страница"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.filter(published=True).order_by("-created_at")[
            :5
        ]
        return context


class PostListView(ListView):
    model = Post
    template_name = "blog_app/post_list.html"
    context_object_name = "posts"
    paginate_by = 3

    def get_queryset(self):
        if query := self.request.GET.get("text"):
            return self.model.objects.filter(title__contains=query)
        else:
            return self.model.objects.filter(published=True)


class PostDetailView(DetailView):
    model = Post
    template_name = "blog_app/post_detail.html"
    context_object_name = "post"

    @method_decorator(cache_page(60 * 1))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        increment_views_count.delay(post_id=self.object.id)
        return response


class CategoriesListView(ListView):
    model = Category
    template_name = "blog_app/categories_list.html"
    context_object_name = "categories"
    paginate_by = 5

    def get_queryset(self):
        return self.model.objects.all()


class CategoryDetailView(DetailView):
    model = Category
    pk_url_kwarg = "category_id"
    template_name = "blog_app/category_detail.html"
    context_object_name = "category"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.filter(
            category=self.object, published=True
        ).order_by("-created_at")
        return context


class PostCreateView(StaffRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog_app/create_post.html"

    def get_success_url(self):
        return reverse("blog:post_detail", args=[self.object.slug])

    def form_valid(self, form):
        form.instance.slug = slugify(form.cleaned_data["title"])
        form.instance.author = self.request.user
        return super().form_valid(form)


class CategoryCreateView(StaffRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "blog_app/create_category.html"

    def form_valid(self, form):
        form.instance.slug = slugify(form.cleaned_data["title"])
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog_app/create_post.html"

    # Ищем по slug статью, или возвращаем ошибку, если нет такого slug
    def get_object(self, queryset=None):
        slug = self.kwargs["slug"]
        return get_object_or_404(Post, slug=slug)

    # Проверяем валидность
    def form_valid(self, form):
        if (
            self.object.title != form.cleaned_data["title"]
        ):  # сравниваем новое и старое название
            form.instance.slug = slugify(
                form.cleaned_data["title"]
            )  # если разные - меняем slug
        return super().form_valid(form)
