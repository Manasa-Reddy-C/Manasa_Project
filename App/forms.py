from django import forms
from App.models import Login
class LoginForm(forms.ModelForm):
    class Meta:
        model=Login
        fields='__all__'