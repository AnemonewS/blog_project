import re
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.core.exceptions import ValidationError
from .models import Category, Post


class AddNews(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title","content","category"]
        widgets = {
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "content":forms.Textarea(attrs={"class":"form-control", "rows": 5}),
            "category":forms.Select(attrs={"class":"form-control", "style":"width: 500px"}),
        }

    def clean_title(self):
        title = self.cleaned_data["title"]
        if re.match(r"\d",title):
            raise ValidationError("Название не должно начинаться с цифры!")
        return title

    def clean_content(self):
        content = self.cleaned_data["content"]
        if re.match(r"\d", content):
            raise ValidationError("Название не должно начинаться с цифры!")
        return content


class UserRegisterForm(UserCreationForm):
    name = forms.CharField(label="Имя",widget=forms.TextInput(attrs={"class":"form-control"}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput(attrs={"class":"form-control"}))


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя",widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Пароль",widget=forms.PasswordInput(attrs={"class":"form.control"}))