from django import forms
from .models import Signup

class EmailSignupForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        "type": "email",
        "class": "form-control",
        "placeholder": "Enter your email (to subscribe our newsletter)"
    }), label="")
    class Meta:
        model = Signup
        fields = ('email', )