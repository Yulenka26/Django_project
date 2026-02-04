from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя отправителя")
    email = models.EmailField(verbose_name="E-mail")
    message = models.TextField(verbose_name="Сообщение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата отправки")

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"

    def __str__(self):
        return f"{self.name} - {self.email}"
