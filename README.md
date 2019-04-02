### Instalamos virtualenv

`pip install virtualenv`

### Creamos el ambiente virtual

`virtualenv workshop`

### Activamos el ambiente virtual

`source bin/activate`

### Instalamos Django por primera vez

(workshop)$: `pip install django`

### Creamos el archivo requirements.txt

(workshop)$: `pip freeze > requirements.txt`

### Iniciamos un nuevo proyecto
django-admin startproject workshop

### Dentro del proyecto

### Corremos las migraciones iniciales de Django
(workshop)$: `python manage.py migrate`

### Iniciamos una nueva app
(workshop)$: `python manage.py startapp core`
* Agrego mi app “core” a installed apps

### Corremos el servidor de Django
(workshop)$: python manage.py runserver
* Lo terminamos con Ctrl + C

### Creamos un superusuario
(workshop)$: python manage.py createsuperuser

### Creamos la primera vista “home” en nuestro archivo views.py de la app “core”
  
### Creamos carpeta de “templates” en el proyecto

### Referenciamos la carpeta templates en APP_DIRS del archivo settings.py

### Creamos modelos Employee y Role

### Creamos las migraciones el servidor
(workshop)$: `python manage.py makemigrations`
 
### Ejecutamos las migraciones 
 
(workshop)$: `python manage.py migrate`
   
