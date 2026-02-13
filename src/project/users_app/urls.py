from django.urls import path

from project.users_app import views

app_name = "users"
urlpatterns = [
    path("", views.ProfileUpdateView.as_view(), name="user_page"),
    path("profile/", views.ProfileDetailView.as_view(), name="user_profile"),
]
