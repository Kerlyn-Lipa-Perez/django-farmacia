from django import forms
from .models import Cliente,Factura,DetalleFactura,Producto



class CreateClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre','direccion','telefono','email']

class CrearProductosForm(forms.ModelForm):

    
    class Meta:
        model = Producto
        fields = ['nombre','descripcion','stock','precio_venta', 'precio_compra','stock']

        widgets = {
             'proveedor': forms.Select(attrs={"class": "form-control"}),
        }

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