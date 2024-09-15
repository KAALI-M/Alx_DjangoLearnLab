from typing import Any
from django import forms
from django.contrib.auth.models import Permission
#from MyUser.models import User
from django.contrib.auth import get_user_model



class RegisterUserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={ 'placeholder': 'enter password'})
    )
    confirmed_password = forms.CharField(
        widget=forms.PasswordInput(attrs={ 'placeholder': 'confirm password'})
    )
    class Meta:
        model = get_user_model()
        exclude = ['password']
    def clean(self):
        cleaned_data = super().clean()
        pwd = cleaned_data.get('password')
        conf_pwd = cleaned_data.get('confirmed_password')
        if not ( pwd and conf_pwd and (conf_pwd == pwd)) :
            self.add_error(None,"Password don't match")
        return cleaned_data
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            # Save the instance to the database
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={ 'placeholder': 'Username'})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )