from django import forms
from .models import Prestamo, Libro

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = '__all__'