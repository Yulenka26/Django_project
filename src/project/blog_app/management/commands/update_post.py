from django.core.management import BaseCommand
from project.blog_app.models import Post


class Command(BaseCommand):
    help = "Изменяет название статьи"

    def handle(self, *args, **options):
        old_title = input("Введите текущее название статьи: ")
        new_title = input("Введите новое название статьи: ")

        updated_title = Post.objects.filter(title=old_title).update(title=new_title)

        if updated_title:
            self.stdout.write(self.style.SUCCESS(f"Название статьи успешно изменено на '{new_title}'!"))
        else:
            self.stdout.write(self.style.ERROR("Статья с названием '{old_title}' не найдена!"))
