from django.forms import ModelForm,Form
from django import forms
from .models import User
class RegisterForm(ModelForm):
    class Meta:
        fields = ['username','email','phone','password']
        model = User
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Hash the password
        if commit:
            user.save()
        return user

class LoginForm(Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)