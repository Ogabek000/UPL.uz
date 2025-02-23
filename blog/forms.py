from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from blog.models import CustomUser, Article


class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control",
        "placeholder":"username"
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control",
        "placeholder":"password"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control",
        "placeholder":"re-password"
    }))

    class Meta:
        model = CustomUser
        fields = ('username','password1','password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control",
        "placeholder":"username"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control",
        "placeholder":"password"
    }))

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','info','photo','category']
        widgets = {
            'title':forms.TextInput(attrs={
                'class':"form-control",
                'placeholder':"title"
            }),
            'info': forms.Textarea(attrs={
                'class': "form-control",
                'placeholder': "Description"
            }),
            'photo': forms.FileInput(attrs={
                'class': "form-control",
            }),
            'category': forms.Select(attrs={
                'class': "form-control",
            }),
        }