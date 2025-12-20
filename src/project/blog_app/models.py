from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
