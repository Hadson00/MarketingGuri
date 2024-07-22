from django import forms
from django.forms import ModelForm
from myapp.models import *

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['title', 'description', 'section']
        labels = {
            'title': "Título:",
            'description': "Descrição:",
            'section': 'Seção:'
            }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'section': forms.Select(attrs={'class':'form-select'})
        }