from django.db import models

class listavideojuegos(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    fecha_lanzamiento = models.DateField()
    plataforma = models.CharField(max_length=50)
