from django.core.checks import messages
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        user_count = User.objects.filter(email = email).count()
        if user_count > 0:
            raise forms.ValidationError("This email has already been registered.")
        return email

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': '', 'placeholder': 'Enter username'})
        self.fields['email'].widget.attrs.update({'class':'', 'placeholder': 'Enter email'})
        self.fields['password1'].widget.attrs.update({'class': '', 'placeholder': 'Enter password'})
        self.fields['password2'].widget.attrs.update({'class': '', 'placeholder': 'Confirm password'})
