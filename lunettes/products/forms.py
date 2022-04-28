from django import forms
from matplotlib import widgets
from .models import *

class ProductForm(forms.ModelForm): 
    class Meta:
        model = Product
        fields = ('name', "description", 'price', 'image', 'gender', 'category') 


        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du Produit'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'price': forms.NumberInput(attrs={'class': 'form-control text-right', 'default': '0.00','step': '0.01', 'min':'0.00'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Image'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
    gender = forms.ModelMultipleChoiceField(queryset=Gender.objects.all(),widget=forms.CheckboxSelectMultiple)
        

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de la catégorie'}),
        }
