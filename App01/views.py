from django.shortcuts import render

def vista1_App01(request):
    return render(request, 'App01/v1.html')

def vista2_App01(request):
    return render(request, 'App01/v2.html')