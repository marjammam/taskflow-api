from django.db import models

# Create your models here.
from proyectos.models import Proyecto

class Tarea(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En progreso'),
        ('completada', 'Completada'),
    ]
    titulo = models.CharField(max_length=200)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='tareas')

    def __str__(self):
        return self.titulo