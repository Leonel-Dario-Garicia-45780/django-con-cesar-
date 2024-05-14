from django.shortcuts import render
# capturar el error si ocurre algo
from django.db import Error
# para devolver errores

# importar modelos
from appprimera_aplicacion_django.models import Producto, Categoria
# Create your views here.

# funciones (@app.route ya no es necesario)

def inicio(request):
    return render (request, "inicio.html")

# funcion agregar categoria, y la vista
def agergar_categoria(request):
    if request.method=='POST':
        try:
            nombre = request.POST["nombre_categoria"]
            categoria= Categoria(get_nombre=nombre)
            categoria.save()
            mensaje= "categoria agregada correctamente"
        except Error as error:
            mensaje=str(error)
        retorno={"mensaje":mensaje}
    
    return render(request, "agregar_categoria.html", retorno)

