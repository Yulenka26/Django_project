from django import forms

from project.users_app.models import Profile


class UsersForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio", "social_link"]
        widgets = {
            "bio": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Расскажите о себе",
                    "rows": "3",
                }
            ),

            "social_link": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ссылка на соцсети",
                }
            ),
        }
