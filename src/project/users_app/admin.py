from django.contrib import admin
from project.users_app.models import Profile

@admin.register(Profile)
class UsersAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "bio", "social_link")
    list_filter = ("user",)
    readonly_fields = ("id", "user", "bio", "social_link")
