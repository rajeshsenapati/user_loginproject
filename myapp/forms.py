from django.core import validators
from django import forms


class UserForm(forms.Form):
    Name = forms.CharField()
    Email = forms.EmailField()
    Password = forms.CharField(widget=forms.PasswordInput)
    Confirmpassword = forms.CharField(widget=forms.PasswordInput)
    Address = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()
        password = self.cleaned_data['Password']
        conpassword = self.cleaned_data['Confirmpassword']
        if password != conpassword:
            raise forms.ValidationError('Password does not match..')
