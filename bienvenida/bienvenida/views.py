from django.http import HttpResponse

def inicio(request):
    nombre = "Vicente García"
    return HttpResponse(f"¡Bienvenidos a mi primera app Django, {nombre}!")
