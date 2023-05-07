# Generated by Django 4.2.1 on 2023-05-03 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id_proveedor', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=200)),
                ('precio_venta', models.DecimalField(decimal_places=2, max_digits=8)),
                ('precio_compra', models.DecimalField(decimal_places=2, max_digits=8)),
                ('stock', models.IntegerField()),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='farmacia.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id_factura', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_emision', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('descuento', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('iva', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='farmacia.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=8)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=8)),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmacia.factura')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='farmacia.producto')),
            ],
        ),
    ]
