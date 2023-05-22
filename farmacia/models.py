# Create your models here.
from django.db import models
from django.core.validators import MinLengthValidator,validate_email,EmailValidator

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=9,validators=[MinLengthValidator(9)])
    email = models.EmailField(max_length=254, validators=[EmailValidator( message='Ingresa un correo valido')])
    def __str__(self):
        return self.nombre



class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    precio_venta = models.DecimalField(max_digits=8, decimal_places=2)
    precio_compra = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()
    
    def __str__(self):
        return self.nombre


class Factura(models.Model):
    id_factura = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT )
    fecha_emision = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    descuento = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    igv = models.DecimalField(max_digits=8, decimal_places=2, default=18)
    def __int__(self):
        return self.id_factura


class DetalleFactura(models.Model): 
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=8, decimal_places=2)
    subtotal = models.DecimalField(max_digits=8, decimal_places=2)
    def __Producto__(self):
        return self.producto

