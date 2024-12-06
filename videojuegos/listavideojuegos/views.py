from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import listavideojuegos









def crear_videojuego(request):
  if request.method == 'POST':
        nombre = request.POST['nombre']
        genero = request.POST['genero']
        plataforma = request.POST['plataforma']
        fecha_lanzamiento = request.POST['fecha_lanzamiento']
        listavideojuegos.objects.create(
            nombre=nombre, genero=genero,
            plataforma=plataforma, fecha_lanzamiento=fecha_lanzamiento
        )
        return HttpResponseRedirect('/inicio')
  return render(request, 'crear.html', {})
  