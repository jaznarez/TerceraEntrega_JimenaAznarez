from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Bienvenido a Mercado Online!")

def segundavista(request):
    return HttpResponse("Cómo podemos ayudarte hoy?")