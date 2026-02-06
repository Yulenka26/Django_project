from django.urls import path
from project.feedback_app import views

app_name = "feedback"
urlpatterns = [
    path('', views.feedback_page, name='feedback_page'),
    path("success/", views.success, name="success"),
]
