"""
URL configuration for frontend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web.views import index, crear_producto, actualizar_producto, eliminar_producto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('producto/crear', crear_producto, name='crear_producto'),
    path('producto/actualizar/<int:id>', actualizar_producto, name='actualizar_producto'),
    path('producto/eliminar/<int:id>', eliminar_producto, name='eliminar_producto'),
]