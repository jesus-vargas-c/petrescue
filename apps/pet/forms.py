from django import forms
from apps.pet.models import Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet

        fields = [
            'name',
            'sexpet',
            'age',
            'rescue_date',
            'person',
            'vaccine',
        ]
        labels ={
            'name': 'Name',
            'sexpet': 'Sex Pet',
            'age': 'Age',
            'rescue_date': 'Rescued',
            'person': 'Owner',
            'vaccine': 'Vaccines',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'sexpet': forms.TextInput(attrs={'class':'form-control'}),
            'age': forms.TextInput(attrs={'class':'form-control'}),
            'rescue_date': forms.TextInput(attrs={'class':'form-control'}),
            'person': forms.Select(attrs={'class':'form-control'}),
            'vaccine': forms.CheckboxSelectMultiple(),
        }

