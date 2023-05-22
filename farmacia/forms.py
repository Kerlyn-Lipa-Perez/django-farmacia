from django import forms
from .models import Cliente,Factura,DetalleFactura,Producto
from django.core.validators import RegexValidator
from django.core.validators import MinLengthValidator,validate_email,EmailValidator
from django.core.exceptions import ValidationError
import re
#Añadir Widgets a todos para que validen los datos de entrada 

class CreateClienteForm(forms.ModelForm):
   
    class Meta:
        model = Cliente
        fields = ['nombre','direccion','telefono','email']
        labels ={
            'nombre': 'Nombre',
            'direccion': 'Direccion',
            'telefono': 'Telefono',
            'email': 'Email'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={"class": "form-control"}),
            'direccion': forms.TextInput(attrs={"class": "form-control"}),
            'telefono': forms.NumberInput(attrs={"class": "form-control"})
        }
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if nombre and not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s]+$', nombre):
            raise ValidationError("El campo 'nombre' solo debe contener letras.")
        return nombre

    def clean_direccion(self):
        direccion = self.cleaned_data.get('direccion')
        if direccion and not re.match(r'^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑüÜ\s]+$', direccion):
            raise ValidationError("El campo 'direccion' solo debe contener letras y números.")
        return direccion


class CrearProductosForm(forms.ModelForm):

    
    class Meta:
        model = Producto
        fields = ['nombre','descripcion','stock','precio_venta', 'precio_compra']
        labels = {
            'nombre':'Nombre',
            'descripcion':'Descripcion',
            'stock':'Stock',
            'precio_venta':'Precio de venta',
            'precio_compra':'Precio de compra'
        }
        widgets = {
            'nombre': forms.Select(attrs={"class": "form-control"}),
            'descripcion': forms.Select(attrs={"class": "form-control","placeholder": "Escriba la descripción"}),

        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if nombre and not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s]+$', nombre):
            raise ValidationError("El campo 'nombre' solo debe contener letras.")
        return nombre

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        if descripcion and not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s]+$', descripcion):
            raise ValidationError("El campo 'descripcion' solo debe contener letras.")
        return descripcion



class CrearFacturasForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all())

    
    class Meta:
        model = Factura  
        fields = ['cliente','total','descuento']
        labels = {
            'cliente':'Cliente',
            'total':'Total de costo',
            'descuento':'Descuento',
        }
        widgets = {
            'cliente': forms.Select(attrs={"class": "form-control"}),

        }
   

            
class CrearDetalleFacturaForm(forms.ModelForm):
    producto = forms.ModelChoiceField(queryset=Producto.objects.all())
    class Meta:
        model = DetalleFactura
        fields = ['producto','cantidad','precio_unitario','subtotal']
        widgets = {
            
  
        }
