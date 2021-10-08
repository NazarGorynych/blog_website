from django import forms
from .models import User
from django.template.defaultfilters import slugify


class UserForm(forms.ModelForm):
    nickname = forms.CharField(label='Nickname')
    email = forms.EmailField(label='Your email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)
    password1 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput, required=True)
    slug = forms.SlugField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = User
        fields = ['nickname', 'email', 'password', ]

    def clean_password1(self):
        password = self.cleaned_data.get('password')
        password1 = self.cleaned_data.get('password1')
        if password and password1 and password != password1:
            msg = 'Passwords don\'t match'
        return password

    def save(self, commit=True):

        User = super(UserForm, self).save(commit=False)
        if commit:
            User.slug = slugify(User.nickname)
            User.save()
        return User