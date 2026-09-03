from django.shortcuts import render

def vista1_app1(request):
    return render(request, 'app1/v1.html')

def vista2_app1(request):
    return render(request, 'app1/v2.html')