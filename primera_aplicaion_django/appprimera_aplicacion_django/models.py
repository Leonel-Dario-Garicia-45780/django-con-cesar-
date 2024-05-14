#!from django.db import models , para miwql y sqlive
from djongo import models


# Create your models here.
# crar los modelos
# ejemplo

class Categoria(models.Model):
    id_categoria=models.CharField(max_length=50, unique=True)
    get_nombre= models.CharField(max_length=30,unique=True)

class Producto(models.Model):
    id_producto=models.CharField(max_length=50, unique=True)
    nombre= models.CharField(max_length=50)
    precio=models.CharField(max_length=10)
    descripcion=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to="imagenes/", null=True, blank=True)
    categoria=models.ForeignKey(Categoria, on_delete=models.PROTECT)






#!
#*
#?
#todo