from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import listavideojuegos

def pagina_inicio(request):
  lista = listavideojuegos.objects.all().values()
  template = loader.get_template('inicio.html')
  context = {
    'lista': lista,
  }
  return HttpResponse(template.render(context, request))

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

