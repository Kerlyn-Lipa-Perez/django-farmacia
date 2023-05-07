from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CreateClienteForm
from .models import Cliente,Factura
from django.db import connection;
# Create your views here.

cursor = connection.cursor()

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

 

# def crear_clientes(request):

    if request.method == 'GET':
         return render(request,'clientes/form.html',{
        'form':CreateClienteForm
        })
    else:
        try:
            CreateClienteForm(request.POST)
            new_cliente = form.save(commit = "false")
            new_cliente.user = request.user
            new_cliente.save()
            return render('clientes/index.html')
        except ValueError:
            return render(request,'clientes/form.html',{
                    'form':CreateClienteForm,
                     'error':'Por favor escribe un valor valido'
                       
                    
                    })

   
    
def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/index.html',{
        'clientes':clientes
    })

def crear_clientesss(request):

    formulario = CreateClienteForm(request.POST or None,  request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('clientes')
    return render(request, 'clientes/crear.html',{
        'formulario' : formulario
    }) 

def editar_clientes(request,id):
    clientes = Cliente.objects.get(id_cliente=id)
    formulario = CreateClienteForm(request.POST or None, request.FILES or None, instance=clientes)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('clientes')

    return render(request,'clientes/editar.html',{
        'formulario':formulario,
    })

def eliminar_clientes(request,id):
    clientes= Cliente.objects.get(id_cliente=id)
    clientes.delete()
    return redirect('clientes')


@login_required
def facturacion(request):
    facturas = Factura.objects.all()

    
    return render(request,'facturacion/index.html')
@login_required
def proveedores(request):
    return render(request,'proveedores/index.html')
@login_required
def productos(request):
    return render(request,'productos/index.html')

