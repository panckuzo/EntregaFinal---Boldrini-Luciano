# Tercera-Pre-entrega---Boldrini
Tercera Pre-entrega del curso de Python en CoderHouse

Este es un proyecto web creado con Django que finalmente sera un E-commerce

Modelos:
- Subcriptores
- Productos
- Provedores
- Reseñas

Formulario:
- Subcriptores
- Crear Productos
- Crear Provedores
- Busqueda y filtrado de Prductos
- Busqueda y filtrado de Provedores
- Reseñas


## Funcionalidades
- Inicio: En el se encuentra el formulario de suscriptores en la página de inicio para recopilar correos electrónicos de los usuarios y realizar marketing por correo electrónico con las personas que deseen recibir noticias, promociones y descuentos.
- Lista de productos y proveedores: La lista de proveedores no se mostrará en la versión final, solo servirá para consultas de administradores y trabajadores de la marca. Los productos en la versión final se mostrarán con imágenes y un botón de comprar para agregar al carrito. Además, se puede realizar la búsqueda y filtrado de productos y proveedores por nombre.
- Crear productos/Proveedores: Esta vista solo está destinada a cumplir con la entrega (no se mostrará en la versión final ya que se supone que los clientes no crean productos ni proveedores y se harán desde la página oculta de administración, donde solo tendrán acceso personas autorizadas).
- Tu opinión: En esta pestaña, los clientes pueden dejar reseñas de productos o cualquier comentario que deseen.


## Instalación

1. Clona este repositorio en tu máquina local.
2. Crea un entorno virtual e instala las dependencias necesarias con `pip install -r requirements.txt`.
3. Ejecuta las migraciones con `python manage.py migrate`.
4. Ejecuta el servidor de desarrollo con `python manage.py runserver`.


## Estructura del Proyecto

- Models.py: Define los modelos de datos de la aplicación.
- Forms.py: Define los formularios de la aplicación.
- Views.py: Define las vistas de la aplicación.
- Urls.py: Define las rutas de la aplicación.
- Inicio.html: Es la plantilla que se utiliza como página de inicio, muestra información de la empresa y el formulario de suscriptores.
- Productos.html: Es la plantilla que se utiliza para mostrar los productos y proveedores.
- Crear.html: Es la plantilla que se utiliza para crear los productos y proveedores.
- Resena.html: Es la plantilla que se utiliza para dejar y mostrar reseñas de productos y opiniones.
