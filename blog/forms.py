from django import forms
from .models import User, Post
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email')

    def user_save(self, commit=True):
        User = super(CustomUserCreationForm, self).save(commit=False)
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


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['author', ]

    def post_save(self, commit=True):
        Post = super(PostForm, self).save(commit=False)
        if commit:
            Post.save()
        return Post

    # def clean_password1(self):
    #     password = self.cleaned_data.get('password')
    #     password1 = self.cleaned_data.get('password1')
    #     if password and password1 and password != password1:
    #         msg = 'Passwords don\'t match'
    #     return password
