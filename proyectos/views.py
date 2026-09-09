import logging
from django.shortcuts import render


# Create your views here.
from rest_framework import viewsets, permissions
from .models import Proyecto
from .serializers import ProyectoSerializer
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProyectoForm

logger = logging.getLogger('taskflow')

class ProyectoViewSet(viewsets.ModelViewSet):
    serializer_class = ProyectoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Cada usuario solo ve sus propios proyectos
        return Proyecto.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        proyecto = serializer.save(usuario=self.request.user)
        logger.info(f"Usuario'{self.request.user.username}' creo el proyecto'{proyecto.nombre}' (id={proyecto.id})")
        
    
    

@login_required
def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.usuario = request.user
            proyecto.save()
            logger.info(f"[Formulario] Usuario'{request.user.username}' creo el proyecto'{proyecto.nombre}' (id={proyecto.id})")
            return redirect('listar_proyectos')
    else:
        form = ProyectoForm()
    return render(request, 'proyectos/form_proyecto.html', {'form': form})


@login_required
def listar_proyectos(request):
    proyectos = Proyecto.objects.filter(usuario=request.user)
    return render(request, 'proyectos/lista_proyectos.html', {'proyectos': proyectos})


@login_required
def detalle_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id, usuario=request.user)
    tareas = proyecto.tareas.all()  
    return render(request, 'proyectos/detalle_proyecto.html', {
        'proyecto': proyecto,
        'tareas': tareas
    })


