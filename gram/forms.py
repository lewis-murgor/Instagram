from django import forms
from .models import Image,Profile,Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['date','profile','likes','comments']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','followers','following']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user','image','pub_date']

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']