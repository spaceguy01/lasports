from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=250, help_text='eg. your-email@anyemail.com')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')
