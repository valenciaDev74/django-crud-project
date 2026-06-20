from django import forms
from django.forms import ModelForm
from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = {"title", "description", "important"}
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter task title"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter description",
                    "rows": 3,
                }
            ),
            "important": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        max_length=30,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter username"}
        ),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Enter password"}
        ),
    )


class SignupForm(forms.Form):
    username = forms.CharField(
        label="Username",
        max_length=30,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter username"}
        ),
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Enter password"}
        ),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Confirm password"}
        ),
    )
