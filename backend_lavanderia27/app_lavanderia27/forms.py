from django import forms
from .models import (
    ArticuloRopa,
    ClienteLavanderia,
    PedidoLavanderia,
    DetallePedidoLavanderia,
    EmpleadoLavanderia,
    MaquinaLavanderia,
    ReporteOperacional
)

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = ArticuloRopa
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = ClienteLavanderia
        fields = '__all__'

class PedidoForm(forms.ModelForm):
    class Meta:
        model = PedidoLavanderia
        fields = '__all__'

class DetalleForm(forms.ModelForm):
    class Meta:
        model = DetallePedidoLavanderia
        fields = '__all__'

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = EmpleadoLavanderia
        fields = '__all__'

class MaquinaForm(forms.ModelForm):
    class Meta:
        model = MaquinaLavanderia
        fields = '__all__'
        widgets = {
            'ultima_revision': forms.DateInput(attrs={'type': 'date'})
        }

class ReporteForm(forms.ModelForm):
    class Meta:
        model = ReporteOperacional
        fields = '__all__'
