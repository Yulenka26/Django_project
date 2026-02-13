from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Профиль")
    bio = models.TextField(verbose_name="Биография")
    social_link = models.URLField(max_length=200, unique=True, verbose_name="Ссылка на внешний сайт")

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        return self.user
