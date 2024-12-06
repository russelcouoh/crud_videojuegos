from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import listavideojuegos






















def actualizar_videojuego(request, id):
    videojuego = get_object_or_404(listavideojuegos, id=id)
    if request.method == 'POST':
        videojuego.nombre = request.POST['nombre']
        videojuego.genero = request.POST['genero']
        videojuego.fecha_lanzamiento = request.POST['fecha_lanzamiento']
        videojuego.plataforma = request.POST['plataforma']
        videojuego.save()
        return redirect('inicio')
    return render(request, 'actualizar.html', {'listavideojuegos': videojuego})