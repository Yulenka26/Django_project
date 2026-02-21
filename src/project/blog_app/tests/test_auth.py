from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from project.blog_app.models import Category, Post


class AuthorisationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='123456789Dj', is_staff=True)
        self.category = Category.objects.create(title='test_category', slug='test_category')

    def test_create_post_anonymous(self):
        response = self.client.get(reverse("blog:create_post"))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("users:login"), response.url)

    def test_create_post_authenticated(self):
        self.client.login(username='test_user', password='123456789Dj')
        response = self.client.get(reverse("blog:create_post"))
        self.assertEqual(response.status_code, 200)

    def test_create_post_submit(self):
        self.client.login(username='test_user', password='123456789Dj')
        response = self.client.post(reverse("blog:create_post"), {
            "title": "test title",
            "content": "test content",
            "category": self.category.pk
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(title="test title").exists())
