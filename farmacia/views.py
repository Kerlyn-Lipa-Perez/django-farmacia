from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CreateClienteForm,CrearProductosForm,CrearFacturasForm,CrearDetalleFacturaForm
from .models import Cliente,Factura,Producto,DetalleFactura
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.



def inicio(request):
    return render(request,'inicio.html')


def signup(request):

    if request.method == 'GET':
        print('Enviando formulario')
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        # verificacion de contraseñas
        if request.POST['password1'] == request.POST['password2']:
            # registrando usuario
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request,user)
                return (redirect('facturacion'))
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'El usuario ya existe'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'Contraseñas no coinciden'
        })

def signout(request):
    logout(request)
    return redirect('inicio')


def signin(request):
    if request.method == 'GET' :
        return render(request,'signin.html',{
        'form':AuthenticationForm
        })
    else:
        user = authenticate(request,username = request.POST['username'], password = request.POST['password'])
        print(request.POST)
        if user  is None:
            return render(request,'signin.html',{
                'form':AuthenticationForm,
                'error':'El usuario o la contraseña es incorrecto'
            })
        else:
            login(request,user)
            return redirect('facturacion')

 

@login_required  
def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/index.html',{
        'clientes':clientes
    })

@login_required
def crear_clientesss(request):
    formulario = CreateClienteForm(request.POST or None,  request.FILES or None)


    if formulario.is_valid():
        formulario.save()
        return redirect('clientes')
    return render(request, 'clientes/crear.html',{
        'formulario' : formulario,

    }) 

@login_required
def editar_clientes(request,id):
    clientes = Cliente.objects.get(id_cliente=id)
    formulario = CreateClienteForm(request.POST or None, request.FILES or None, instance=clientes)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('clientes')

    return render(request,'clientes/editar.html',{
        'formulario':formulario,
    })

@login_required
def eliminar_clientes(request,id):
    clientes= Cliente.objects.get(id_cliente=id)
    clientes.delete()
    return redirect('clientes')



@login_required
def productos(request):
    productos = Producto.objects.all()
    return render(request,'productos/index.html',{
        'productos': productos
    })

@login_required
def crear_producto(request):
    formulario = CrearProductosForm(request.POST or None, request.FILES or None)
    
    if formulario.is_valid():
        formulario.save()
        return redirect('productos')
    return render(request, 'productos/crear.html',{
        'formulario': formulario,

    })

@login_required
def editar_producto(request,id):
    productos=Producto.objects.get(id_producto= id)
    formulario = CrearProductosForm(request.POST or None, request.FILES or None, instance=productos)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('productos')

    return render(request, 'productos/editar.html',{
        'formulario':formulario
    })

@login_required
def eliminar_producto(request,id):
    clientes = Producto.objects.get(id_producto = id)
    clientes.delete()
    return redirect('productos')

@login_required
def facturacion(request):
    facturas = Factura.objects.all()
    return render(request,'facturacion/index.html',{
        'facturas': facturas
    })

@login_required
def crear_facturas(request):
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()
    detalle_facturas = DetalleFactura.objects.all()
    formulario = CrearFacturasForm(request.POST or None, request.FILES or None)
    formularioooo = CrearDetalleFacturaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid() and formularioooo.is_valid():
        factura = formulario.save() 
        detalle_factura = formularioooo.save(commit=False) 
        detalle_factura.factura = factura 
        detalle_factura.save()  
        return redirect('facturacion')

    return render(request, 'facturacion/crear.html',{
        'formulario': formulario,
        'formularioooo':formularioooo,
        'clientes': clientes,
        'detalle_facturas':detalle_facturas,
        'productos':productos
    })

@login_required
def eliminar_facturas(request,id):
    facturas = Factura.objects.get(id_factura = id)
    facturas.delete()
    return redirect('facturacion')

@login_required
def editar_facturas(request,id):
    factura=Factura.objects.get(id_factura= id)
    cliente = factura.cliente #
    print(cliente)
    formulario = CrearFacturasForm(request.POST or None, request.FILES or None, instance=factura)
    formulario.fields['cliente'].initial = cliente
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('facturacion')

    return render(request, 'facturacion/editar.html',{
        'formulario':formulario,
        'factura': factura,
        'cliente': cliente

    })

