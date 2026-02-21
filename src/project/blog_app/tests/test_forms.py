from django.test import TestCase

from project.blog_app.forms import PostForm
from project.blog_app.models import Category


class PostFormTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(title='test_category', slug='test_category')

    def test_valid_form(self):
        data = {
            'title': 'test_title',
            'category': self.category,
            'content': 'test_content'
        }
        form = PostForm(data=data)
        self.assertTrue(form.is_valid())

    def test_empty_title(self):
        data = {
            'title': '',
            'category': self.category,
            'content': 'test_content'
        }
        form = PostForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)

    def test_empty_content(self):
        data = {
            'title': 'test_title',
            'category': self.category,
            'content': ''
        }
        form = PostForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("content", form.errors)
