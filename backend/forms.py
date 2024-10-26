from django import forms
from django.contrib.auth.models import User
from .models import Order

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UpdateQuantityForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['quantity']
