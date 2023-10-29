from django.shortcuts import render

def inicio(request):
    return render(request, "inicio.html")

def nosotros(request):
    return render(request, "nosotros.html")

def shop(request):
    return render(request, "shop.html")





