from django import forms
from .models import User

class UserFrom(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nome','telefone','email']