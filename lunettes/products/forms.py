from django import forms
from .models import *

class ProductForm(forms.ModelForm): 
    class Meta:
        model = Product
        fields = ('name', "description", 'price', 'image', 'gender') 

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du Produit'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prix'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Image'}),
            'gender': forms.Select(attrs={'class':'form-control'})
        }
