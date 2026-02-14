from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class CustomCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Придумайте пароль",
                "autocomplete": "new-password",
            }
        )
    )
    password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Подтвердите пароль",
                "autocomplete": "new-password",
            }
        )
    )
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите имя пользователя",
                    "autocomplete": "username",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите ваш email",
                    "autocomplete": "email",
                }
            ),
        }

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Пользователь с таким Email уже зарегистрирован. Введите другой Email.")
        return email
