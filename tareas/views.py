from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Tarea
from .serializers import TareaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TareaForm

class TareaViewSet(viewsets.ModelViewSet):
    serializer_class = TareaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Solo tareas de proyectos que pertenecen al usuario autenticado
        return Tarea.objects.filter(proyecto__usuario=self.request.user).select_related('proyecto')


class TareasPendientesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tareas = Tarea.objects.filter(
            proyecto__usuario=request.user,
            estado='pendiente'
        ).select_related('proyecto')
        serializer = TareaSerializer(tareas, many=True)
        return Response(serializer.data)



@login_required
def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST, usuario=request.user)
        if form.is_valid():
            form.save()
            return redirect('listar_tareas')
    else:
        form = TareaForm(usuario=request.user)
    return render(request, 'tareas/form_tarea.html', {'form': form})


@login_required
def listar_tareas(request):
    tareas = Tarea.objects.filter(proyecto__usuario=request.user).select_related('proyecto')
    return render(request, 'tareas/lista_tareas.html', {'tareas': tareas})