"""djangoProject3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Models.Categoria.views import formularioCategoriaView
from Models.Marca.views import formularioMarcaView
from Models.Producto.views import formularioProductoView
from Views.HomeView import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView.home,name='home'),
    path('registrarCategoria/',formularioCategoriaView.index,name='registrarCategoria'),
    path('guardarCategoria/', formularioCategoriaView.procesar_formulario, name='guardarCategoria'),
    path('registrarMarca/', formularioMarcaView.indexmarc, name='registrarMarca'),
    path('guardarMarca/', formularioMarcaView.procesar_formulariomarca, name='guardarMarca'),
    path('registrarProducto/', formularioProductoView.index, name='registrarProducto'),
    path('guardarProducto/', formularioProductoView.procesar_formularioproduc, name='guardarProducto'),
    path('listaProducto/', formularioProductoView.listar_producto, name='listarProducto'),
    path('editarProducto/<int:id_producto>', formularioProductoView.edit, name='editarProductos'),
    path('actualizarProducto/<int:id_producto>', formularioProductoView.actualizar, name='actualizarProductos'),
    path('eliminarProducto/<int:id_producto>', formularioProductoView.delete, name='eliminarProductos'),
]
