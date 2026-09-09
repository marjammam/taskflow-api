
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProyectoViewSet, crear_proyecto, listar_proyectos, detalle_proyecto

router = DefaultRouter()
router.register(r'proyectos', ProyectoViewSet, basename='proyecto')

urlpatterns = [
    path('proyectos/nuevo/', crear_proyecto, name='crear_proyecto'),
    path('proyectos/lista/', listar_proyectos, name='listar_proyectos'),
    path('proyectos/<int:proyecto_id>/', detalle_proyecto, name='detalle_proyecto'),
] + router.urls