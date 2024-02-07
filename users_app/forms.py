from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CostumRegisterForm(UserCreationForm):
    email=forms.EmailField()#mandatory field, if not mandatory wrute (requried=false)
    
    
    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2']#the fields that apear in the form in this order
    