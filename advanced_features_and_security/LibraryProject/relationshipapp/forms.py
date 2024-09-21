from typing import Any
from django import forms
from django.contrib.auth.models import Permission
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm



class CustomUserCreationForm(UserCreationForm):

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={ 'placeholder': 'enter password'})
    )
    confirmed_password = forms.CharField(
        widget=forms.PasswordInput(attrs={ 'placeholder': 'confirm password'})
    )
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
        label='Date of Birth',
        help_text='Please use the format YYYY-MM-DD'
    )
    class Meta:
        model = get_user_model()
        fields = ['username', 'email','date_of_birth', 'profile_photo']
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

class CustomUserChangeForm(UserChangeForm):
    current_password = forms.CharField(
        widget=forms.PasswordInput(attrs={ 'placeholder': 'enter current password'})
    )
    new_password = forms.CharField(required= False,
        widget=forms.PasswordInput(attrs={ 'placeholder': 'enter new password'})
    )
    confirmed_password = forms.CharField(required= False,
        widget=forms.PasswordInput(attrs={ 'placeholder': 'confirm password'})
    )
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
        label='Date of Birth',
        help_text='Please use the format YYYY-MM-DD'
    )
    change_password = forms.BooleanField(
        required=False,
        label='Change Password',
        widget=forms.CheckboxInput(attrs={'id': 'id_change_password'})
    )
    class Meta:
        model = get_user_model()
        fields = ['username', 'email','date_of_birth', 'profile_photo']
    def clean(self):
        user = self.instance
        cleaned_data = super().clean()
        currpwd = cleaned_data.get('current_password')
        pwd = cleaned_data.get('new_password')
        conf_pwd = cleaned_data.get('confirmed_password')
        if not user.check_password(currpwd) : 
            self.add_error('current_password',f"the current password is incorrect,{currpwd}, {user.check_password(currpwd)}")
        return cleaned_data
            
    def save(self, commit=True):
        user = super().save(commit=False)
        cleaned_data = super().clean()
        pwd = cleaned_data.get('new_password')
        conf_pwd = cleaned_data.get('confirmed_password')
        ch_pw= cleaned_data.get('change_password')
        if ch_pw and pwd and conf_pwd and (conf_pwd == pwd):  #the password is changed if they are bot entred and matched
            user.set_password(self.cleaned_data['new_password'])
        else:
             self.add_error(None,"passwords don't match")
        if commit:
            # Save the instance to the database
                       user.save()
        return user


class RegisterUserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={ 'placeholder': 'enter password'})
    )
    confirmed_password = forms.CharField(
        widget=forms.PasswordInput(attrs={ 'placeholder': 'confirm password'})
    )
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
        label='Date of Birth',
        help_text='Please use the format YYYY-MM-DD'
    ) 

    class Meta:
        model = get_user_model()
        fields = ['username', 'email',  'profile_photo']
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