from django import forms
from .models import product

class productmanagement(forms.ModelForm):
    class Meta:
        model = product
        fields = "__all__"
