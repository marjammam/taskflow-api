# TaskFlow API

## Descripción del proyecto

TaskFlow es una aplicación backend desarrollada con **Django** y **Django REST Framework** para la gestión de proyectos y tareas. Permite a cada usuario registrarse, iniciar sesión y administrar sus propios proyectos y tareas de forma aislada, con autenticación mediante **JWT** (Access Token y Refresh Token).

El proyecto incluye:
- CRUD completo de Proyectos y Tareas (vía API REST y vía formularios web de Django).
- Autenticación y autorización con JWT.
- Restricción de recursos por usuario autenticado.
- Documentación interactiva con Swagger/OpenAPI.
- Logging de acciones relevantes.
- Pruebas automatizadas.

## Requisitos previos

- Python 3.10 o superior
- MySQL 8.0 o superior (probado con MySQL Workbench)
- Git

## Instalación de dependencias

1. Clona el repositorio:
```bash
git clone https://github.com/marjammam/taskflow-api.git
cd taskflow-api
```

2. Crea y activa un entorno virtual:
```bash
python -m venv venv
```
Windows:
```bash
venv\Scripts\activate
```
Linux/Mac:
```bash
source venv/bin/activate
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Configuración de variables de entorno

Crea un archivo `.env` en la raíz del proyecto (este archivo está incluido en `.gitignore` y no debe subirse al repositorio) con el siguiente contenido:

```
SECRET_KEY=tu-clave-secreta-django
DEBUG=True
DB_NAME=taskflow_db
DB_USER=root
DB_PASSWORD=tu_password_mysql
DB_HOST=127.0.0.1
DB_PORT=3306
```

> Para un entorno de producción, cambia `DEBUG=False`.

## Configuración de la base de datos

1. Abre MySQL Workbench (o el cliente de tu preferencia) y crea la base de datos:
```sql
CREATE DATABASE taskflow_db CHARACTER SET utf8mb4;
```

2. Asegúrate de que las credenciales en tu archivo `.env` coincidan con tu configuración local de MySQL.

## Ejecución de migraciones

Con el entorno virtual activado, ejecuta:
```bash
python manage.py makemigrations
python manage.py migrate
```

## Creación del superusuario

```bash
python manage.py createsuperuser
```
Sigue las instrucciones en pantalla para definir usuario, correo y contraseña.

## Ejecución del servidor de desarrollo

```bash
python manage.py runserver 5050
```

La aplicación quedará disponible en `http://127.0.0.1:5050/accounts/login/`.

> Nota: si el puerto 5050 está ocupado, puedes usar cualquier otro puerto libre, por ejemplo `python manage.py runserver 8090`.

## Acceso a la documentación de la API (Swagger/OpenAPI)

Con el servidor corriendo, accede a:
- Swagger UI: `http://127.0.0.1:5050/swagger/`
- Redoc: `http://127.0.0.1:5050/redoc/`

## Autenticación JWT

- **Registro de usuario:** `POST /api/registro/`
- **Obtener token (login):** `POST /api/token/`
```json
{
  "username": "tu_usuario",
  "password": "tu_contraseña"
}
```
- **Refrescar token:** `POST /api/token/refresh/`
```json
{
  "refresh": "tu_refresh_token"
}
```

Para acceder a los endpoints protegidos, incluye el header:
```
Authorization: Bearer <access_token>
```

## Endpoints principales

| Método | Endpoint | Descripción |
|---|---|---|
| GET/POST | `/api/proyectos/` | Listar / crear proyectos del usuario autenticado |
| GET/PUT/DELETE | `/api/proyectos/{id}/` | Detalle, actualizar o eliminar un proyecto |
| GET/POST | `/api/tareas/` | Listar / crear tareas del usuario autenticado |
| GET/PUT/DELETE | `/api/tareas/{id}/` | Detalle, actualizar o eliminar una tarea |
| GET | `/api/tareas/pendientes/` | Listar tareas pendientes del usuario autenticado |
| POST | `/api/registro/` | Registro de nuevo usuario |
| POST | `/api/token/` | Login (obtener access y refresh token) |
| POST | `/api/token/refresh/` | Renovar access token |

## Vistas con formularios (Django tradicional)

| Ruta | Descripción |
|---|---|
| `/accounts/login/` | Inicio de sesión (punto de entrada de la interfaz web) |
| `/api/proyectos/lista/` | Lista de proyectos del usuario logueado |
| `/api/proyectos/nuevo/` | Formulario para crear un proyecto |
| `/api/proyectos/{id}/` | Detalle de un proyecto con sus tareas |
| `/api/tareas/nueva/` | Formulario para crear una tarea |
| `/api/tareas/lista/` | Lista de tareas del usuario logueado |

## Cómo ejecutar las pruebas

```bash
python manage.py test proyectos
```

Esto ejecuta las pruebas automatizadas que verifican:
- Que un usuario no autenticado no puede acceder a los recursos protegidos.
- Que un usuario autenticado solo puede ver sus propios proyectos.

## Logging

El proyecto registra eventos relevantes (como la creación de proyectos) tanto en consola como en el archivo `taskflow.log`, generado en la raíz del proyecto al ejecutar la aplicación.

## Seguridad y buenas prácticas aplicadas

- Variables sensibles gestionadas mediante `.env` (excluido del control de versiones).
- Contraseñas de usuario hasheadas automáticamente por Django.
- Autenticación JWT en todos los endpoints protegidos.
- Restricción de recursos: cada usuario solo puede ver y modificar sus propios proyectos y tareas.
- Uso de `select_related()` para optimizar consultas relacionadas.
- Protección CSRF en formularios web.
