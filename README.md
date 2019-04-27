# django-crash-workshop (ejercicios)

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


### (En caso de que sea un proyecto existente) Leemos el archivo requirements.txt

(workshop)$: `pip install -r requirements.txt`

### Iniciamos un nuevo proyecto
(workshop)$: `django-admin startproject workshop`

### Dentro del proyecto

### Corremos las migraciones iniciales de Django
(workshop)$: `python manage.py migrate`

### Iniciamos una nueva app
(workshop)$: `python manage.py startapp movies`
* Agrego mi app “movies” a installed apps

### Corremos el servidor de Django
(workshop)$: python manage.py runserver
* Lo terminamos con Ctrl + C

### Creamos un superusuario
(workshop)$: python manage.py createsuperuser

### Creamos la primera vista “home” en nuestro archivo views.py de la app “movies”
  
### Creamos carpeta de “templates” en el proyecto

### Referenciamos la carpeta templates en APP_DIRS del archivo settings.py

### Creamos modelos Employee y Role

### Creamos las migraciones el servidor
(workshop)$: `python manage.py makemigrations`
 
### Ejecutamos las migraciones 
 
(workshop)$: `python manage.py migrate`
   
