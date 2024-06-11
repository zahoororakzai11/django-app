from django.forms import forms
#import model
from .models import Products

class ProductionForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = [
            'title',
            'content',
            'price'
        ]