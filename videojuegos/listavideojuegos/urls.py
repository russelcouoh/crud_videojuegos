from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.pagina_inicio, name='inicio'),
    path('crear/', views.crear_videojuego, name='crear_videojuego'),
    path('actualizar/<int:id>/', views.actualizar_videojuego, name='actualizar_videojuego'),
    path('borrar/<int:id>/', views.borrar_videojuego, name='borrar_videojuego'),
    
]
