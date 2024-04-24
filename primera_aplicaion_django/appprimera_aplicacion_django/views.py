from django.shortcuts import render

# Create your views here.

# funciones (@app.route ya no es necesario)

def inicio(request):
    return render (request, "inicio.html")


