from django.db import models

# Create your models here.
# crar los modelos
# ejemplo
class Producto(models.Model):
    getid=models.CharField(max_length=50,unique=True)
    get_nombre= models.CharField(max_length=50)
