from django.http import HttpRequest
from django.shortcuts import render

from Models.Categoria.models import Categoria
from Models.Categoria.forms import FormularioCategoria


class formularioCategoriaView(HttpRequest):

    def index(request):
        categoria = FormularioCategoria()
        return render(request,'Categoria.html',{"form":categoria})

    def procesar_formulario(request):
        categoria = FormularioCategoria(request.POST)
        if categoria.is_valid():
            categoria.save()
            categoria= FormularioCategoria()


        return render(request, "Categoria.html", {"form": categoria, "mensaje": "ok"})

    def listar_Categoria(request):
        categoria = Categoria.objects.all()
        return render(request, "Listar.html", {"Categoria": categoria})