from django.apps import AppConfig


class NinjaApiConfig(AppConfig):
    name = 'project.ninja_api'
    def ready(self):
        import project.ninja_api.signals # noqa - не ругайся
