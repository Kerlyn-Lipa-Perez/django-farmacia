from django import forms
from .models import Cliente,Factura,DetalleFactura



class CreateClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre','direccion','telefono','email']

class CrearFormulario(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['cliente','total','descuento','igv'] 

class CrearDetalleFormulario(forms.ModelForm):
    class Meta:
        model = DetalleFactura
        fields =['cantidad','precio_unitario','subtotal',]
