from django.core.management import BaseCommand

from project.blog_app.models import Post


class Command(BaseCommand):
    help = "Выводит опубликованные статьи"

    def handle(self, *args, **options):
        posts = Post.objects.filter(published=True).order_by("id")[:3]

        if not posts.exists():
            self.stdout.write("Нет опубликованных статей")
            return

        for post in posts:
            self.stdout.write(f"{post.id} {post.title} {post.created_at:%d.%m.%Y}")
