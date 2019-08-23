from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import hashlib

from app.models import Post, Profile

class SignUpUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
        )
        widgets = {'password': forms.PasswordInput()}
    
    def __init__(self, *args, **kwargs):
        super(SignUpUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['email'].widget.attrs['placeholder'] = 'E-mail'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'

class SignUpProfileForm(forms.ModelForm):
    image = forms.FileField()
    class Meta:
        model = Profile
        fields = (
            "about_me",
        )
    
    def __init__(self, *args, **kwargs):
        super(SignUpProfileForm, self).__init__(*args, **kwargs)
        self.fields['about_me'].widget.attrs['placeholder'] = 'About Me'

class ToPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "title",
            "subtitle",
            "lide",
            "text",
            "image"
        )

    def __init__(self, *args, **kwargs):
        super(ToPostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'Title'
        self.fields['subtitle'].widget.attrs['placeholder'] = "Subtitle"
        self.fields['lide'].widget.attrs['placeholder'] = "Lide"
        self.fields['text'].widget.attrs['placeholder'] = "Text"

