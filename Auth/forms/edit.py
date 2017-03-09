from django import forms
from django.forms import widgets
from django.contrib.auth.forms import UserChangeForm

from Auth.models import User, Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'characters', 'description', 'profile_picture', 'dob', 'gender')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')
