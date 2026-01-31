from django import forms
from project.blog_app.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "author", "published", "category"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "palceholder": "Введите название статьи"
                }
                ),
            "author": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "palceholder": "Введите статью",
                    "rows": 10
                }
            ),
            "category": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),
            "published": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input"
                }
            ),
        }
