from django.contrib import admin
from .models import Cliente,Proveedor,Producto,Factura,DetalleFactura
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Factura)
admin.site.register(DetalleFactura)