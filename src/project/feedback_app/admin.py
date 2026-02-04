from django.contrib import admin
from project.feedback_app.models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "created_at")
    list_filter = ("created_at",)
    readonly_fields = ("id", "name", "email", "created_at")
