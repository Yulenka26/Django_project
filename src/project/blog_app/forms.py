from django import forms
from project.blog_app.models import Post, Category


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "author", "published", "category"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите название статьи"
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
                    "placeholder": "Введите статью",
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

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")

        if Post.objects.filter(title=title).exists():
            raise forms.ValidationError(f"Статья с названием '{title}' уже существует. Введите другое название статьи")

        return cleaned_data


class SearchForm(forms.Form):
    query = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Поиск статей"
            }
        )
    )

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["title"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите название категории"
                }
                )
        }
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")

        if Category.objects.filter(title=title).exists():
            raise forms.ValidationError(f"Категория '{title}' уже существует. Введите другое название категории")

        return cleaned_data
