# Entrega Final---Boldrini Luciano
Entrega Final curso de Python con Django 

Modelos:
- Subcriptores
- Productos
- Provedores
- Reseñas
- User

Formulario:
- Subcriptores
- Crear Productos
- Crear Provedores
- Busqueda y filtrado de Prductos
- Busqueda y filtrado de Provedores
- Reseñas


## Funcionalidades
- Inicio: En el se encuentra el formulario de suscriptores en la página de inicio para recopilar correos electrónicos de los usuarios y realizar marketing por correo electrónico con las personas que deseen recibir noticias, promociones y descuentos.
-Productos: permite publicar productos y ver la lista de productos. Si se esta logeado se puede publicar, editar y eliminar productos. Sin logear solo se ver y buscar producos y el detalle de los mismos.
-Proveedores: permite publicar proveedores y ver la lista de proveedores publicados. Si se esta logeado se puede publicar, editar y eliminar provedores. Sin logear solo se ver y buscar producos y el detalle de los mismos
- Tu opinión: En esta pestaña, los clientes pueden dejar reseñas de productos o cualquier comentario que deseen.
- Registrarse
- Ver perfil, donde se accede a editar el msismo y cambio de contraseña
- Login
-Logout


## Instalación

1. Clona este repositorio en tu máquina local.
2. Crea un entorno virtual e instala las dependencias necesarias con `pip install -r requirements.txt`.
3. Ejecuta las migraciones con `python manage.py migrate`.
4. Ejecuta el servidor de desarrollo con `python manage.py runserver`.


## Estructura del Proyecto

- Models.py: Define los modelos de datos de la aplicación.
- Forms.py: Define los formularios de la aplicación.
- Views.py: Define las vistas de la aplicación. (con funciones y clases basadas en vistas)
- Urls.py: Define las rutas de la aplicación.
- Templates: plantilla predefinida para generar contenido dinámico

