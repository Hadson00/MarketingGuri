from django import forms
from django.forms import ModelForm
from myapp.models import *

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['title', 'path', 'description']
        labels = {
            'title': "Título:",
            'path': "Faça upload:",
            'description': "Descrição:",     
            }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo'}),
            'path': forms.ClearableFileInput(attrs={'class': 'form-control',}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }