from django import forms
from .models import Image,Profile

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['date','profile','likes','comments']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']