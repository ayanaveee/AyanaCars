from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['title', 'model', 'engine_volume', 'color', 'transmission', 'category','year_of_manufacture', 'price', 'location', 'registration', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
