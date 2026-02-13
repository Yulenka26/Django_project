from django.urls import reverse_lazy
from django.views.generic import UpdateView

from project.users_app.models import Profile


class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ["bio", "social_link"]
    template_name = "users_app/user_page.html"
    success_url = reverse_lazy("users:user_page")

    # Проверяем, есть ли профиль. если нет - создаем
    def get_object(self, queryset=None):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile
