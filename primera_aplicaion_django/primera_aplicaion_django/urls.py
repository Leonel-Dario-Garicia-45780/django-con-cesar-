"""
URL configuration for primera_aplicaion_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# importamos vew
from appprimera_aplicacion_django import views

# mas importaciones
from django.conf import settings
from django.conf.urls.static import static

# url son las vistas o paginas

urlpatterns = [
    path('admin/', admin.site.urls),
    #la funcion inicio que esta en views.py
    path('', views.inicio ),# esta es la ruta raiz
    path('agregar_categoria/', views.agregar_categoria), # ruta de agregar categoria
    path('eliminar_categoria/', views.eliminar_categoria   ),
    path('agregar_producto/',  views.agregar_producto ),
    path('vista_agregar_producto/',  views.vista_agregar_productos),#? ruta gregada por el instructor Cesar
    path('lista_productos/',   views.lista_productos  ),
    path('editar_producto/',   views.editar_producto  ),
 #   path('eliminar_producto/',   views.eliminar_producto  ),

]


# debug
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

