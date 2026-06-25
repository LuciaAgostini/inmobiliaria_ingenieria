# TP Evaluativo - Ingeniería de Software (2026)
# Inmobiliaria San Martín

Este proyecto es un sistema web para la gestión de una inmobiliaria desarrollado en Django para la primera mitad del año. Implementa la arquitectura MVT, manejo de base de datos relacional, control de accesos por grupos y usuarios personalizados.

---

# Requisitos del proyecto

# 1. Base de datos y Modelos
El sistema cuenta con un esquema de 6 modelos relacionados entre sí para cubrir la lógica del negocio:
* **Usuario Personalizado:** Se utilizó `AbstractUser` desde el inicio del proyecto para extender la autenticación por defecto de Django.
* **Propiedad:** Modelo para la gestión de los inmuebles (casas, departamentos, terrenos). Incluye el campo `ImageField` para la carga de fotos.
* **Cliente:** Registro y datos de contacto de los clientes.
* **Atención:** Registro para el seguimiento y las consultas personalizadas de los clientes.
* **Categoría:** Clasificación para el tipo de propiedad.
* **Localidad:** Datos geográficos para la ubicación de los inmuebles.

# 2. Autenticación y Usuarios
* El registro de nuevos usuarios se realiza directamente desde los templates de la web.
* El login y el logout son completamente funcionales desde las plantillas personalizadas.

# 3. Vistas y ABM (CRUD)
* Se integró una barra de navegación común en el frontend para moverse por todo el sitio.
* Desarrollamos el ABM completo (crear, ver, editar y borrar) desde la interfaz web para los módulos de **Propiedades** y **Clientes**.
* El panel de administración (`admin.py`) quedó configurado con buscadores, ordenamiento y filtros por campos clave.

# 4. Permisos y Seguridad
* **Manejo de Roles:** Se configuraron grupos de usuarios para segmentar los accesos (por ejemplo, Agentes y Clientes).
* **Protección de rutas:** Las vistas de modificación (crear, editar, borrar) están restringidas según los permisos del grupo, mientras que las vistas de consulta básica requieren únicamente estar logueado.

# 5. Estilos y Context Processor
* La interfaz fue diseñada con CSS logrando un diseño limpio, con tarjetas para las propiedades y mensajes de alerta integrados.
* Se incluyó un Context Processor personalizado para pasar datos globales a los templates de forma automática.
* La carga y el renderizado de las imágenes de las propiedades funcionan correctamente.

---

# Capturas de pantalla del sistema

*(Nota: Las imágenes están guardadas en la raíz del repositorio con estos nombres)*

# Inicio
(Captura desde 2026-06-25 00-51-51.png)

# Catálogo de Propiedades (Vista pública)
Captura desde 2026-06-25 00-52-04.png)

# Gestión de Propiedades (Botones)
(Captura desde 2026-06-25 00-52-28.png)

# Panel de Clientes
(Captura desde 2026-06-25 00-52-46.png)

1. Clonar el repositorio:
   bash
   git clone <url_del_repositorio>
   cd inmobiliaria

Crear y activar el entorno virtual:
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Linux/macOS:
source venv/bin/activate

Instalar las dependencias (Django y Pillow para las imágenes):
pip install django pillow

Ejecutar las migraciones de la base de datos:
python manage.py makemigrations
python manage.py migrate

Crear el usuario administrador:
python manage.py createsuperuser

Levantar el servidor de desarrollo:
python manage.py runserver

Entrar en el navegador a: http://127.0.0.1:8000/
































---

