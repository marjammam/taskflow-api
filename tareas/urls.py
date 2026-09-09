
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TareaViewSet, TareasPendientesView, crear_tarea, listar_tareas

router = DefaultRouter()
router.register(r'tareas', TareaViewSet, basename='tarea')

urlpatterns = [
    path('tareas/pendientes/', TareasPendientesView.as_view(), name='tareas-pendientes'),
    path('tareas/nueva/', crear_tarea, name='crear_tarea'),
    path('tareas/lista/', listar_tareas, name='listar_tareas'),
] + router.urls