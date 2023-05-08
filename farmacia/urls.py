from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.inicio , name="home"),
    path('signup/',views.signup, name="signup"),
    path('inicio/',views.inicio, name="inicio"),
    path('logout/',views.signout, name="logout"),
    path('signin/',views.signin, name="signin"),

    path('clientes',views.clientes, name="clientes"),
    path('clientes/crear',views.crear_clientesss, name="crear"),
    path('clientes/editar',views.editar_clientes, name="editar-clientes"),
    path('clientes/eliminar/<int:id>/',views.eliminar_clientes, name="eliminar_clientes"),
    path('clientes/editar/<int:id>/',views.editar_clientes, name="editar_clientess"),    

    path('facturacion',views.facturacion, name="facturacion"),
    path('facturacion/crear',views.crear_facturas, name="crear-facturas"),
    path('facturacion/editar',views.editar_facturas, name="editar-facturas"),
    path('facturacion/eliminar/<int:id>/',views.eliminar_facturas, name="eliminar-facturas"),
    path('facturacion/editar/<int:id>/',views.editar_facturas, name="editar-facturas"),

    path('productos',views.productos, name="productos"),
    path('productos/crear',views.crear_producto, name="crear-producto"),
    path('productos/eliminar/<int:id>',views.eliminar_producto, name="eliminar-producto"),
    path('productos/editar',views.editar_producto, name="editar-productos"),
    path('productos/editar/<int:id>',views.editar_producto, name="editar-producto"),

]
