from django.apps import AppConfig


class BlogAppConfig(AppConfig):
    name = "project.blog_app"

    def ready(self):
        import project.blog_app.signals  # noqa
