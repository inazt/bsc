from django import forms

class AuthLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
