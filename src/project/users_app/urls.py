from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, reverse_lazy

from project.users_app import views

app_name = "users"
urlpatterns = [
    path("", views.ProfileUpdateView.as_view(), name="user_page"),
    path("profile/", views.ProfileDetailView.as_view(), name="user_profile"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("password_change/", PasswordChangeView.as_view(
        template_name="users_app/password_change.html",
        success_url=reverse_lazy("users:password_change_done")),
        name="password_change"),
    path("password_change_done/", PasswordChangeDoneView.as_view(
        template_name="users_app/password_change_done.html"),
         name="password_change_done"),
    path('password_reset/', PasswordResetView.as_view(
        template_name='users_app/password_reset.html',
        email_template_name='users_app/password_reset_email.html', # <-- Указываем свой шаблон письма
        success_url=reverse_lazy('users:password_reset_done')),
        name='password_reset'),
    path('password_reset_done/', PasswordResetDoneView.as_view(
        template_name='users_app/password_reset_done.html'),
        name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='users_app/password_reset_confirm.html',
        success_url=reverse_lazy('users:password_reset_complete')),
        name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(
        template_name='users_app/password_reset_complete.html'),
        name='password_reset_complete'),
]
