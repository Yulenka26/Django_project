from django.urls import reverse_lazy
from django.views.generic import UpdateView, DetailView

from project.users_app.forms import UsersForm
from project.users_app.models import Profile


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = UsersForm
    template_name = "users_app/user_page.html"
    success_url = reverse_lazy("users:user_profile")

    # Проверяем, есть ли профиль. если нет - создаем
    def get_object(self, queryset=None):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

class ProfileDetailView(DetailView):
    model = Profile
    template_name = "users_app/user_profile.html"
    context_object_name = "profile"

    # Показываем профиль пользователя
    def get_object(self):
        return self.request.user.profile
