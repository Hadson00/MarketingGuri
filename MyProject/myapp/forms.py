from django import forms
from django.forms import ModelForm
from myapp.models import *

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['title', 'path', 'description', 'section']
        labels = {
            'title': "Título:",
            'path': "Faça upload:",
            'description': "Descrição:",
            }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo'}),
            'path': forms.ClearableFileInput(attrs={'class': 'form-control',}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'section': forms.Select(attrs={'class':'form-select'})
        }


# from django import forms
# from .models import Trip, Country

# class TripForm(forms.ModelForm):
#     class Meta:
#         model = Trip
#         fields = ['name', 'country', 'start_date', 'end_date']

    
#     country = forms.ModelChoiceField(
#         queryset=Country.objects.all(),
#         to_field_name='name',
#         required=True,  
#         widget=forms.Select(attrs={'class': 'form-control'})
#     )