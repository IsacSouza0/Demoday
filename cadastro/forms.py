from django import forms
from cadastro.models import Cadastro

class CadastroCriarForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = [
            'nome',
            'email',
            # 'telefone',
        ]