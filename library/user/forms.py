from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm # predifine components is imported to create forms


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() # Email field is compulsory

    class Meta:
        model = User
        # field will be printed and also with this sequence in the form instance on template.
        fields = ['username', 'email', 'password1', 'password2']
