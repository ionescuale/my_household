from django import forms
from django.forms import TextInput, Textarea

from household.models import Household


class HouseholdForm(forms.ModelForm):
    class Meta:
        model = Household
        fields = ['name', 'description']

    widgets = {
        'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of the household'}),
        'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Introduce a short description of the household'})
    }
