
# Create your tests here.
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Proyecto


class ProyectoAPITestCase(APITestCase):
    def setUp(self):
        # Creamos dos usuarios distintos para probar el aislamiento de recursos
        self.usuario1 = User.objects.create_user(username='usuario1', password='ClaveSegura123')
        self.usuario2 = User.objects.create_user(username='usuario2', password='ClaveSegura123')

        self.proyecto_usuario1 = Proyecto.objects.create(
            nombre='Proyecto de Usuario 1',
            descripcion='Descripción de prueba',
            usuario=self.usuario1
        )

    def _obtener_token(self, username, password):
        response = self.client.post('/api/token/', {
            'username': username,
            'password': password
        })
        return response.data['access']

    def test_usuario_no_autenticado_no_puede_ver_proyectos(self):
        """Un usuario sin token no debe poder acceder a la lista de proyectos."""
        response = self.client.get('/api/proyectos/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_usuario_solo_ve_sus_propios_proyectos(self):
        """Un usuario autenticado no debe ver proyectos de otro usuario."""
        token = self._obtener_token('usuario2', 'ClaveSegura123')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        response = self.client.get('/api/proyectos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # usuario2 no tiene proyectos propios, así que la lista debe estar vacía
        self.assertEqual(len(response.data), 0)