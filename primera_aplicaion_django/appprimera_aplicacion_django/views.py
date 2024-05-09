from django.shortcuts import render
# capturar el error si ocurre algo
# para devolver errores
from django.db import Error
from bson import ObjectId

# importar modelos
from appprimera_aplicacion_django.models import Producto, Categoria
# Create your views here.

#! //////////////////////////////////////////////////////////////
#? utilizar la extencion "Better Comments" para mejor lectura
#! //////////////////////////////////////////////////////////////


# funciones (@app.route ya no es necesario)

def inicio(request):
    return render (request, "inicio.html")

#todo lo relacionado con categorias

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

def eliminar_categori(request):
    return render(request, "" )

#todo fin de todo lo relacionado con categorias

#? //////////////////////////////////////////////////////////////

#todo lo relacionado con productos (por el momento lo no pongo relaciones porque no logor resolver esos errores)

def vista_agregar_productos(request):
    categorias=Categoria.objects.all()
    retorno={"categorias":categorias}
    return render(request, "agregar_producto.html", retorno )


def agregar_producto(request):
    mensaje=""
    if request.method=="POST":
        try:
            id            = request.POST["id"]
            nombre_objeto        = request.POST["nombre"]
            precio_objeto        = request.POST["precio"]
            decripcion_objeto    = request.POST["desceipcion"]
            imagen_objeto        = request.FILES["imagen"]
            #id_categoria  = ObjectId(request.POST["id_categoria"]) 

            print("ID:", id)
            print("Nombre:", nombre_objeto)
            print("Precio:", precio_objeto)
            print("Descripción:", decripcion_objeto)
            print("Imagen:", imagen_objeto)
            # print("ID de Categoría:", id_categoria)


            #categoria_objeto = Categoria.objects.get(pk=str(id_categoria))

            producto=Producto.objects.create(
                id_producto = id,
                nombre      = nombre_objeto,
                precio      = precio_objeto,
                descripcion = decripcion_objeto,
                imagen      = imagen_objeto
                #categoria   = categoria_objeto 
            )

            mensaje="producto agregado correctamente"
            print(mensaje)
        except Error as error:
            mensaje=str(error)
    
    #! esto es para el select del html
    categorias=Categoria.objects.all()
    retorno={"mensaje":mensaje, "categorias":categorias}
    return render(request, "agregar_producto.html", retorno )


def lista_productos(request):
    productos=Producto.objects.all()
    print(productos)
    retorno={"productos":productos}
    return render(request, "lista_productos.html", retorno)

def editar_producto(request):
    id_prodicto_editado= ObjectId(request.POST['id_producto'])

    producto_editado= Producto.objects.get(pk=id_prodicto_editado)
    producto_editado.nombre=
    producto_editado.precio=
    producto_editado.descripcion=
    producto_editado.imagen=
    producto_editado.categoria=

    return render(request, ""  )

#todo fin de todo lo relacionado con productos (sin relaciones para evitar errores)
