from django.shortcuts import render

# Create your views here.

def retorna_index(request):
    return render(request, 'index.html')