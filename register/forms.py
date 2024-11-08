from django import forms
from django.contrib.auth.forms import UserCreationForm

class Register(UserCreationForm):
    first_name = forms.CharField(max_length= 200, required= True)
    last_name = forms.CharField(max_length= 200, required= True)
    email = forms.EmailField(required= True)
    profile_photo = forms.ImageField()
