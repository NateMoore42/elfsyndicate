from django import forms
from django.contrib.auth import authenticate

from Auth.models import User

class AuthenticationForm(forms.Form):
    email = forms.EmailField(widget=forms.widgets.TextInput)
    password = forms.CharField(widget=forms.widgets.PasswordInput)

    class Meta:
        fields = ['email', 'password']

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        user = authenticate(email=email, password=password)
        if user is None:
            raise forms.ValidationError("Sorry, those details don't belong to anyone. Make sure you've spelled everything correctly.")
        if not user.is_active:
            raise forms.ValidationError('Your account has been disabled.')
        return self.cleaned_data

    def login(self, request):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        user = authenticate(email=email, password=password)
        return user
