from django.core.management import BaseCommand
from project.blog_app.models import Post


class Command(BaseCommand):
    help = "Удаляет статью"

    def handle(self, *args, **options):
        try:
            id_to_del = int(input("Введите id статьи для удаления: "))
        except ValueError:
            self.stdout.write(self.style.ERROR("Ошибка: введите корректный числовой id"))
            return

        try:
            post = Post.objects.get(id=id_to_del)
        except Post.DoesNotExist:
            self.stdout.write(self.style.WARNING(f"Статья с id {id_to_del} не найдена. Введите верный id."))
            return

        post.delete()
        self.stdout.write(self.style.SUCCESS(f"Статья с id {id_to_del} успешно удалена!"))
