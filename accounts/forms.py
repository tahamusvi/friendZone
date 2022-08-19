from django import forms
from .models import *
from django.contrib.auth.forms import ReadOnlyPasswordHashField

#------------------------------------------------------------------------------------------------
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='password confirm',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','name')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise forms.ValidationError('password must match')
        return cd['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
#------------------------------------------------------------------------------------------------
class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
    password = forms.CharField(max_length=40,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))
#------------------------------------------------------------------------------------------------
class UserRegistrationForm(forms.Form):
    # username = forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
    name = forms.CharField(max_length=80,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Full name'}))
    password = forms.CharField(max_length=40,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))
