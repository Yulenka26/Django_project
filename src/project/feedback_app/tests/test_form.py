from django.test import TestCase
from django.urls import reverse
from project.feedback_app.models import Feedback


class FeedbackPostTest(TestCase):

    def test_create_feedback_valid_data(self):
        url = reverse("feedback:feedback_page") # открываем страницу ОС

        data = {
            'name': 'test_user',
            'email': '123@mail.ru',
            'message': 'test_message',
            'subject': 'other',
        } # заполняем форму верными данными

        response = self.client.post(url, data) # типа отправляем форму

        self.assertEqual(response.status_code, 302)  # проверяем редирект на страницу success, если форма заполнена верно
        self.assertRedirects(response, reverse("feedback:success")) # проверяем, что перекинуло именно на страницу success

        self.assertEqual(Feedback.objects.count(), 1) # проверяем, что появилась новая запись

    def test_create_feedback_invalid_data(self):
        url = reverse("feedback:feedback_page")

        data = {
            'name': 'test_user',
            'email': '',
            'message': 'test_message',
            'subject': 'other',
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)  # редиректа нет, т.к нет почты
        self.assertEqual(Feedback.objects.count(), 0) # проверяем, что не создалось записи

        self.assertIn('email', response.context['form'].errors)
