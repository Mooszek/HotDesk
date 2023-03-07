from django import forms
from .models import User, Profile
from django.contrib.auth.forms import UserCreationForm

COMPANY_EMAIL = '@gmail.com'

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField()

    def clean_email(self):
        data = self.cleaned_data['email']
        if COMPANY_EMAIL not in data:
            raise forms.ValidationError("Must be a company email address!")
        return data

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField()

    def clean_email(self):
        data = self.cleaned_data['email']
        if COMPANY_EMAIL not in data:
            raise forms.ValidationError("Must be a company email address!")
        return data

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']