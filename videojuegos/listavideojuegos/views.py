from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import listavideojuegos

































def borrar_videojuego(request, id):
    videojuego = get_object_or_404(listavideojuegos, id=id)
    if request.method == 'POST':
        videojuego.delete()
        return redirect('inicio')
    return render(request, 'borrar.html', {'listavideojuegos': videojuego})

   