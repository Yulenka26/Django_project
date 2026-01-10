from django.core.management import BaseCommand
from project.blog_app.models import Post, Category
from django.contrib.auth import get_user_model
from slugify import slugify


User = get_user_model()

class Command(BaseCommand):
    help = "Создает новую статью"

    def handle(self, *args, **options):
        title = input("Введите название статьи: ")
        content = input("Введите текст статьи: ")
        author_name = input("Введите имя автора: ")
        category_name = input("Введите название категории: ")

        #находит автора/категорию или создает новую
        author, created = User.objects.get_or_create(username=author_name)

        category_slug = slugify(category_name)
        category, created = Category.objects.get_or_create(title=category_name, defaults={'slug': category_slug})

        slug = slugify(title)

        Post.objects.create(
            title=title,
            content=content,
            author=author,
            category=category,
            slug=slug
        )

        self.stdout.write(self.style.SUCCESS(f'Создана новая статья - "{title}".'))
