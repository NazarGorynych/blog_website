from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.template.defaultfilters import slugify



class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email')

    def save(self, commit=True):
        User = super(UserCreationForm, self).save(commit=False)
        if commit:
            User.save()
        return User


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    # def clean_password1(self):
    #     password = self.cleaned_data.get('password')
    #     password1 = self.cleaned_data.get('password1')
    #     if password and password1 and password != password1:
    #         msg = 'Passwords don\'t match'
    #     return password
