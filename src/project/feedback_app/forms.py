from django import forms
from .models import one_choice

class FeedbackForm(forms.Form):
    name = forms.CharField(
        label="Ваше имя",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите Ваше имя"
            }
        )
    )

    email = forms.EmailField(
        label="Ваш E-mail",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите Ваш E-mail"
            }
        )
    )

    message = forms.CharField(
        label="Ваше сообщение",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Введите Ваше сообщение",
                "rows": "5",
            }
        )
    )

    subject = forms.TypedChoiceField(
        label="Тема обращения",
        choices=one_choice,
        widget=forms.Select(
            attrs={
                "class": "form-select"
            }
        )
    )
