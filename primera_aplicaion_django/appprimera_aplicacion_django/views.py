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
def agregar_categoria(request):
    mensaje=""
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


def agregar_producto(request):
    mensaje=""
    if request.method=="POST":
        try:
            id            = request.POST["id"]
            nombre_objeto        = request.POST["nombre"]
            precio_objeto        = request.POST["precio"]
            decripcion_objeto    = request.POST["desceipcion"]
            imagen_objeto        = request.POST["imagen"]
            id_categoria  = request.POST["id_categoria"]
            categoria_objeto     = Categoria.objects.get(get_nombre=id_categoria)

            producto=Producto.objects.create(
                id_producto = id,
                nombre      = nombre_objeto,
                precio      = precio_objeto,
                descripcion = decripcion_objeto,
                imagen      = imagen_objeto,
                categoria   = categoria_objeto
            )

            mensaje="producto agregado correctamente"
            print(mensaje)
        except Error as error:
            mensaje=str(error)
    
    #! esto es para el select del html
    categorias=Categoria.objects.all()
    retorno={"mensaje":mensaje, "categorias":categorias}
    return render(request, "agregar_producto.html", retorno )

