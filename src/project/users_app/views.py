from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DetailView, CreateView

from project.users_app.forms import ProfileForm, CustomLoginForm, CustomUserCreationForm
from project.users_app.models import Profile


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "users_app/user_page.html"
    success_url = reverse_lazy("users:user_profile")

    # Показываем профиль пользователя
    def get_object(self):
        return self.request.user.profile

class ProfileDetailView(DetailView):
    model = Profile
    template_name = "users_app/user_profile.html"
    context_object_name = "profile"

    def get_object(self, queryset=None):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "users_app/register.html"
    success_url = reverse_lazy("users:user_profile")

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = "users_app/login.html"

    def get_success_url(self):
        return reverse_lazy("users:user_profile")
