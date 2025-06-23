# forms/user.py

from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 'email', 'first_name', 'last_name',
            'is_active', 'is_staff', 'is_superuser', 'groups'
        ]
        widgets = {
            'groups': forms.CheckboxSelectMultiple()
        }
