from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistroSerializer

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistroForm

class RegistroView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = RegistroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"mensaje": "Usuario creado correctamente"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def registro_web(request):
        if request.method == 'POST':
            form = RegistroForm(request.POST)
            if form.is_valid():
                usuario = form.save()
                login(request, usuario)  # inicia sesión automáticamente tras registrarse
                return redirect('listar_proyectos')
        else:
            form = RegistroForm()
        return render(request, 'usuarios/registro.html', {'form': form})