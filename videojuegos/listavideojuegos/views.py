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

  