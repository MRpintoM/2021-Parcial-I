from django.http import HttpRequest
from django.shortcuts import render

from Models.Producto.forms import FormularioProducto
from Models.Producto.models import Producto


class formularioProductoView(HttpRequest):

    def index(request):
        producto = FormularioProducto()
        return render(request,'Producto.html',{"form":producto})

    def procesar_formularioproduc(request):
        producto = FormularioProducto(request.POST)
        if producto.is_valid():
            producto.save()
            producto= FormularioProducto()


        return render(request, "Producto.html", {"form": producto, "mensaje": "ok"})

    def listar_producto(request):
        producto = Producto.objects.all()
        return render(request,"Listar.html",{"productos":producto})

    def edit(request,id_producto):
        producto = Producto.objects.filter(id=id_producto).first()
        form= FormularioProducto(instance=producto)
        return render(request,"Productoedit.html",{"form":form, 'producto':producto})
    def actualizar(request, id_producto ):
        producto = Producto.objects.get(pk=id_producto)
        form= FormularioProducto(request.POST,instance=producto)
        if form.is_valid():
            form.save()
        form= Producto.objects.all()
        return render(request,"Listar.html",{"productos":producto})

    def delete(request,id_producto):
        producto = Producto.objects.get(pk=id_producto)
        producto.delete()
        producto = Producto.all()
        return render(request ,"Listar.html",{"productos":producto})
