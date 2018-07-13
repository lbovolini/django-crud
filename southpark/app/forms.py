from django import forms
from .models import Character

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ('first_name', 'last_name', 'gender', 'age', 'occupation', 'image')