from django.shortcuts import render
from cadastro.forms import CadastroCriarForm

# Create your views here.

def novo_cadastro(request):
    formulario = CadastroCriarForm(request.POST or None)

    if formulario.is_valid():
        formulario.save()
        formulario = CadastroCriarForm()

    context = {
        'form': formulario
    }

    return render(request, 'cadastro.html', context)