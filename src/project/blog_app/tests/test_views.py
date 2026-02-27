from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from project.blog_app.models import Category, Post


class PostViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='123456789Dj')
        self.category = Category.objects.create(title='test_category', slug='test_category')
        self.post = Post.objects.create(title='test_title', slug='test_slug', content='test_content',
                                        category=self.category, author=self.user, published=True)

    def test_index_status_code(self):
        response = self.client.get(reverse("blog:index"))
        self.assertEqual(response.status_code, 200)

    def test_index_template(self):
        response = self.client.get(reverse("blog:index"))
        self.assertTemplateUsed(response, "blog_app/index.html")

    def test_index_contains_post(self):
        response = self.client.get(reverse("blog:index"))
        self.assertContains(response, self.post.title)

    def test_post_detail_status_code(self):
        response = self.client.get(reverse("blog:post_detail", args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_template(self):
        response = self.client.get(reverse("blog:post_detail", args=[self.post.slug]))
        self.assertTemplateUsed(response, "blog_app/post_detail.html")

    def test_post_detail_context(self):
        response = self.client.get(reverse("blog:post_detail", args=[self.post.slug]))
        self.assertEqual(response.context["post"], self.post)

    def test_post_detail_404(self):
        response = self.client.get(reverse("blog:post_detail", args=["Page-does-not-exist"]))
        self.assertEqual(response.status_code, 404)

    def test_index_not_have_unpublished(self):
        Post.objects.create(title='test_title2', slug='test_slug2', content='test_content',
                                        category=self.category, author=self.user, published=False)
        response = self.client.get(reverse("blog:index"))
        self.assertNotContains(response, "test_title2")
        self.assertContains(response, "test_title")

class CategoryViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test_user", password="123456789Dj")

        self.cat_3 = Category.objects.create(title='test_category3', slug='test-category3')
        self.cat_4 = Category.objects.create(title='test_category4', slug='test-category4')

        self.post_3 = Post.objects.create(title='test_title3', slug='test_slug3', content='test_content',
                                             category=self.cat_3, author=self.user, published=True)
        self.post_4 = Post.objects.create(title='test_title4', slug='test_slug4', content='test_content',
                                             category=self.cat_4, author=self.user, published=True)

    def test_filtration(self):
        url = reverse("blog:category_detail", kwargs={"category_id": self.cat_3.id})
        response = self.client.get(url)

        self.assertContains(response, "test_title3")
        self.assertNotContains(response, "test_title4")

    def test_category_id_does_not_exist(self):
        url = reverse("blog:category_detail", kwargs={"category_id": 666})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
