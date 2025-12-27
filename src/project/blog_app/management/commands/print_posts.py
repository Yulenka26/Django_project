from django.core.management import BaseCommand

from project.blog_app.models import Post


class Command(BaseCommand):
    help = "Выводит список постов"

    def handle(self, *args, **options):
        posts = Post.objects.all()

        if not posts.exists():
            self.stdout.write(self.style.WARNING("Статей нет"))
        for post in posts:
            self.stdout.write(f"{post.id} {post.title} {post.created_at:%d-%m-%Y}")
