# Generated by Django 4.2.1 on 2023-05-08 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmacia', '0005_alter_detallefactura_producto_alter_factura_igv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='proveedor',
        ),
        migrations.DeleteModel(
            name='Proveedor',
        ),
    ]