from django import forms
from cadastro.models import Cadastro

class CadastroCriarForm(forms.ModelForm):
   
    
    class Meta:
        model = Cadastro
        labels = {
            "descricao": "Descrição"
        }
        fields = [
            'foto',
            'nome',
            'email',
            # 'telefone', 
            'descricao',
        ]