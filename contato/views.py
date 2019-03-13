from django.shortcuts import render

# Create your views here.

def retorna_contato(request):
    return render(request, 'contato.html')