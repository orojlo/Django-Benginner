from django import forms
from django.contrib.auth.models import User
from MyApp7.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfo(forms.ModelForm):
    class Meta():
        model = userProfileInfo
        fields = ('portfolio_site','profile_pic')
