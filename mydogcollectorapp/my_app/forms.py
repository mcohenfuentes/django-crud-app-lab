from django import forms
from .models import Climb

class ClimbForm(forms.ModelForm):
    class Meta:
        model = Climb
        fields = ['date', 'difficulty']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }