from django.shortcuts import render

# Create your views here.
def perfil_uno(request):
    data= {"nombre": "Latto", "año": 1998, "correo" : "example@mail.com"}
    return render(request, 'perfil/p1.html', data)
def perfil_dos(request):
    data= {"nombre": "Paloma Mami", "año": 1999, "correo" : "example@mail.com", "foto" :"palomita.png" }
    return render(request, 'perfil/p2.html', data)