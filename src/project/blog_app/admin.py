from django.contrib import admin

from project.blog_app.models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug", "content", "author", "published", "created_at", "updated_at")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "content")
    list_filter = ("author", "published", "created_at")
