**Crear un proyecto de Django**
```
django-admin startproject nombre_proyecto
```  
  
**Crear una aplicación**
```
python manage.py startapp nombre_app
```  
  
**Agregar la aplicación al proyecto de Django en settings.py**  
```python  

INSTALLED_APPS = [
    ...,
    'nombre_app'
]
```   
  
**Configurar las URL de la aplicación en urls.py**  
```python   
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ruta', view, name='nombre_ruta'),
    ...
]
```
  
**Ejecutar proyecto Django**
```  
python manage.py runserver
```