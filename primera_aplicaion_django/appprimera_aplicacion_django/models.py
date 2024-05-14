from django.db import models
#! con misql


# Create your models here.
# crar los modelos
# ejemplo
class Categoria(models.Model):
    get_nombre= models.CharField(max_length=30,unique=True)
    

class Producto(models.Model):
    getid=models.CharField(max_length=50,unique=True)
    get_nombre= models.CharField(max_length=50)
    






#!
#*
#?
#todo