from django.shortcuts import render, redirect
# capturar el error si ocurre algo
# para devolver errores
from django.db import Error
from bson import ObjectId
import os
from django.conf import settings

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
            id= request.POST["id_categoria"]
            nombre = request.POST["nombre_categoria"]
            categoria= Categoria(
                id_categoria=id,
                get_nombre=nombre
                )
            categoria.save()
            mensaje= "categoria agregada correctamente"
        except Error as error:
            mensaje=str(error)

    retorno={"mensaje":mensaje}
    return render(request, "agregar_categoria.html", retorno)

#! no funciona y no se porque
""" def eliminar_categoria(request, ):
    mensaje = ""
    categorias=Categoria.objects.all().values()#? correccion 1 agregado el values
    retorno={"categorias":categorias}
    if request.method=='POST':
        eliminar= request.POST["categoria_eliminar"]
        try:
            # Buscamos la categoría por su id
            categoria = Categoria.objects.get(get_nombre=eliminar)
            # Eliminamos la categoría
            categoria.delete()
            mensaje = "Categoría eliminada correctamente"

        except Exception as error:
            mensaje = str(error)
    
    # Redireccionar a la página de listar categorías
    return render(request, "eliminar_categoria.html", retorno) """

#! otra forma
#! tampoco sirve
def eliminar_categoria(request):
    mensaje=""
    try:
        cate_eliminar= request.POST['categoria_eliminar']
        print(cate_eliminar)
        categoria=Categoria.objects.get(get_nombre= cate_eliminar)
        categoria.delete()
        mensaje="categoria eliminada"
        print(mensaje)
    except Exception as error:
        mensaje = str(error)

    return render(request, "eliminar_categoria.html" )
#todo fin de todo lo relacionado con categorias

#? //////////////////////////////////////////////////////////////

#todo lo relacionado con productos (por el momento lo no pongo relaciones porque no logor resolver esos errores)
# ?   correcciones del instructor Cesar
def vista_agregar_productos(request):
    categorias=Categoria.objects.all().values()#? correccion 1 agregado el values
    retorno={"categorias":categorias}
    return render(request, "agregar_producto.html", retorno )


def agregar_producto(request):
    mensaje=""
    if request.method=="POST":
        try:
            id            = request.POST["id"]
            nombre_objeto        = request.POST["nombre"]
            precio_objeto        = request.POST["precio"]
            decripcion_objeto    = request.POST["descripcion"]
            imagen_objeto        = request.FILES["imagen"]
            #? tener en cuenta, para mysql y sqlite
            #? id_categoria = int(request.POST["id_categoria"])
    #        id_categoria  = ObjectId(request.POST["id_categoria"]) #! para mongodb

#            print("ID:", id)
#            print("Nombre:", nombre_objeto)
#            print("Precio:", precio_objeto)
#            print("Descripción:", decripcion_objeto)
#            print("Imagen:", imagen_objeto)
#            print("ID de Categoría:", id_categoria)

    #        categoria_objeto = Categoria.objects.get(pk=id_categoria)

            producto=Producto.objects.create(
                id_producto = id,
                nombre      = nombre_objeto,
                precio      = precio_objeto,
                descripcion = decripcion_objeto,
                imagen      = imagen_objeto,
    #            categoria   = categoria_objeto 
            )
            #? correccion 2 , salvar productos, sin eso ugial funciono que raro
            # linea nueva
            producto.save()
#? fin de las correcciones en este archivo  
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
    try:
        id_prodicto_editado= ObjectId(request.POST['id_producto'])

        producto_editado= Producto.objects.get(pk=id_prodicto_editado)
        producto_editado.nombre=request.POST['nombre_producto_editado']
        producto_editado.precio=request.POST['precio_producto_editado']
        producto_editado.descripcion=request.POST['descripcion_producto_editado']
        imagen_edit=request.FILES['imagen_producto_editado']
        if(imagen_edit):
            if(producto_editado.imagen !=""):
                os.remove(os.path.join(settings.MEDIA_ROOT+"/"+str(producto_editado.imagen)))
            producto_editado.imagen=imagen_edit
        
        #producto_editado.categoria=

        producto_editado.save()
        mensaje="productoeditado correctamente"
    except Error as error:
        mensaje=str(error)

    retorno={"mensaje":mensaje}
    return render(request, "editar_producto.html", retorno  )


def eliminar_producto(request):
    try:
        1
    except Error as error:
        mensaje=str(error)

#todo fin de todo lo relacionado con productos (sin relaciones para evitar errores)
