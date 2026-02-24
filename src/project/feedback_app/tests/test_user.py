from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from project.users_app.models import Profile


class ProfileSignalTest(TestCase):
    def test_profile_created_on_user_creation(self):
        user = User.objects.create_user(username="test_user", password="123456789Dj") # создаем нового пользователя

        profile_exists = Profile.objects.filter(user=user).exists() # проверяем, что для него создался профиль
        self.assertTrue(profile_exists)

class ProfilePrivacyTest(TestCase):
    def test_anonymous_redirected_to_login(self):
        url = reverse("users:user_page")  # страница редактирование профиля
        response = self.client.get(url) # пытаемся ее редактировать

        self.assertEqual(response.status_code, 302) # статус редиректа, т.к. не залогинились

        self.assertIn("/user/login/", response.url) # Редиректит на страницу логина

        self.assertIn("?next=", response.url) # ?next= показывает, куда вернётся после логина,т.е. обратно на страницу
