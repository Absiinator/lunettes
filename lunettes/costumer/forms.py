from django import forms
from matplotlib import widgets
from .models import *

class GenderForm(forms.ModelForm): 
    class Meta:
        model = Gender
        fields = ('name',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de la catégorie'}),
        }

class CostumerForm(forms.ModelForm):
    class Meta:
        model = Costumer
        fields = ('username', 'gender', 'image')

        widgets  = {
            'username' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'gender' : forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Image'}),
        }