from django import forms
from django.contrib.auth.models import User

from .models import Cat, Dipricing


class CatForm(forms.ModelForm):

    class Meta:
        model = Cat
        fields = ['nameKu', 'nameEg', 'image']

class DipricingForm(forms.ModelForm):
    
    class Meta:
        model = Dipricing
        fields = ['food', 'title', 'price', 'start_date', 'exp_date']
