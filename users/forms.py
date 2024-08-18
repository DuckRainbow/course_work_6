from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from mail.forms import FormStyleMixin
from users.models import User


class UserRegisterForm(FormStyleMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']


class UserUpdateForm(FormStyleMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ['email', 'password',]
