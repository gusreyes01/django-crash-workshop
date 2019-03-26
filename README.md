# django-crash-workshop


### Acabas de abrir un nuevo centro digital de renta de películas y requieres exponer tu catálogo de títulos disponibles y que tus clientes puedan rentar a través de el. ¡Manos a la obra!

1.1. Crea un ambiente virtual para tu proyecto utilizando Python3

1.2. Instala los requerimientos incluidos en el archivo requirements.txt

1.3. Genera una nueva base de datos con las tablas iniciales de Django 2.0

1.4. Crea una nueva app inicial para tu proyecto

1.5. Crea un modelo *Peliculas*
  * Agrega los siguientes atributos:
     * Nombre Película (CharField)
     * Reseña (TextField)
     * Genero (CharField choice)
     * Stock (PositiveIntegerField)
     * Disponible (BooleanField)
  * Crea una propiedad en el modelo Películas que calcule el número de disponible en base a los títulos ya rentados.
  
1.6. Crea un modelo *Rentas*
  * Crea un Foreign Key a Usuarios para que puedas guardar las rentas de los usuarios.
      * Crea un Foreign Key a Películas para que puedas indicar que peelícula rentaron.
      
1.8. Crea un listado del catalogo de películas disponibles.

1.9. Crea una vista de login para tus usuarios.

1.10. Habilita las vistas de administración de películas para que el staff dar de alta nuevos títulos.

1.11. Crea un botón de rentar que permita a los usuarios rentar si aún hay stock disponible. En caso de que no, se deberá notificar un error.

1.12. Crea un formulario para que los clientes puedan dejar sugerencias de Películas que quieran que sean agregadas al catálogo.

### Uno de tus clientes (VideoCentro) quiere exponer tus títulos desde su sitio web.

2.0 Crea una propiedad ```as_list_item_dict``` en el modelo *Películas* .

2.1 Utiliza la Crea un endpoint que liste las Películas disponibles.

2.2 Crea un endpoint para permitir rentar desde el sitio web. (Asegurate de poder identificar quién realizó la renta).


