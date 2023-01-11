from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailInput, PasswordInput
from .models import Profile


class NewUserForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }

    # def clean_email(self):
    #     if Profile.objects.filter(email=self.cleaned_data['email']).exists():
    #         raise forms.ValidationError("the given email is already registered")
    #     return self.cleaned_data['email']


class LoginForm(forms.Form):
    email = forms.CharField(max_length=50, widget=EmailInput(
        attrs={'required': 'true', 'placeholder': 'Enter Your email', 'class': 'form-control', 'id': 'email'}))
    password = forms.CharField(min_length=5, max_length=30, widget=PasswordInput(
        attrs={'required': 'true', 'placeholder': 'Enter your password', 'class': 'form-control', 'id': 'review'}))
