from django.db import models

one_choice = [
    ("improve", "Предложить улучшения"),
    ("article", "Предложить статью"),
    ("other", "Другое"),
]
class Feedback(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя отправителя")
    email = models.EmailField(verbose_name="E-mail")
    message = models.TextField(verbose_name="Сообщение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата отправки")
    subject = models.CharField(max_length=100, choices=one_choice, verbose_name="Тема обращения")


    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"

    def __str__(self):
        return f"{self.name} - {self.email}"
