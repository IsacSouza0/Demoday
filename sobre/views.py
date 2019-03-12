from django.shortcuts import render

# Create your views here.

def retorna_sobre(request):
    return render(request, 'sobre.html')