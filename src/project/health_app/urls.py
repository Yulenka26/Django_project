from django.urls import path

from project.health_app import views

app_name = "health_app"
urlpatterns = [
    path('health/', views.HealthView.as_view(), name='health'),
]
