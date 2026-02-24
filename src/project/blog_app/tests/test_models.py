from django.contrib.auth.models import User
from django.test import TestCase
from django.db import IntegrityError

from project.blog_app.models import Category, Post


class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='123456789Dj')
        self.category = Category.objects.create(title='test_category', slug='test_category')
        self.post = Post.objects.create(title='test_title', slug='test_slug', content='test_content',
                                        category=self.category, author=self.user)

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'test_title')
        self.assertEqual(self.post.slug, 'test_slug')
        self.assertEqual(self.post.category, self.category)
        self.assertFalse(self.post.published) # проверяем, что не опубликована

    def test_post_str(self):
        self.assertEqual(str(self.post), "test_title")

class CategoryModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='123456789Dj')
        self.category = Category.objects.create(title='test_category', slug='test_category')

    def test_category_creation(self):
        self.assertEqual(self.category.title, 'test_category')
        self.assertEqual(self.category.slug, 'test_category')

    def test_category_str(self):
        self.assertEqual(str(self.category), "test_category")

    def test_category_slug_unique(self):
        with self.assertRaises(IntegrityError): # проверяет, возникнет ли ошибка. если возникнет - все верно
            Category.objects.create( # создаем еще одну категорию
                title='another_category', # но с другим названием
                slug='test_category'  # пишем тот же slug
            )
