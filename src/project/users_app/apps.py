from django.apps import AppConfig


class UsersAppConfig(AppConfig):
    name = 'project.users_app'
    def ready(self):
        import project.users_app.signals # noqa
