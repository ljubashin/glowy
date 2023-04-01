from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'placeholder':'Email'}))
    username = forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'placeholder':'Username'}))
    password1 = forms.CharField(max_length=100,
                           widget= forms.PasswordInput
                           (attrs={'placeholder':'Password'}))
    password2 = forms.CharField(max_length=100,
                           widget= forms.PasswordInput
                           (attrs={'placeholder':'Repeat Password'}))
    class Meta:
        model = User
        fields =('username', 'email', 'password1', 'password2')