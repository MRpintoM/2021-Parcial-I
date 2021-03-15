from django.http import HttpRequest
from django.shortcuts import render

from Models.Marca.forms import FormularioMarca



class formularioMarcaView(HttpRequest):

    def indexmarc(request):
        marca = FormularioMarca()
        return render(request,'Marca.html',{"form":marca})

    def procesar_formulariomarca(request):
        marca = FormularioMarca(request.POST)
        if marca.is_valid():
            marca.save()
            marca= FormularioMarca()


        return render(request, "Marca.html", {"form": marca, "mensaje": "ok"})


