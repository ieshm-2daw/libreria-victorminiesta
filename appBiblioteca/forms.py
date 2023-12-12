from django import forms
from .models import Prestamo

class prestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['libro_prestado', 'fecha_prestamo', 'fecha_devolucion', 'usuario_prestamo', 'estado']