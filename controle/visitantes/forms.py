from django import forms

class VisitanteForm(forms.Form):
    nome = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite o nome',
            'class': 'form-control'
        })
    )
    cpf = forms.CharField(
        max_length=14,
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite o CPF',
            'class': 'form-control'
        })
    )
    chegada = forms.TimeField(
        widget=forms.TimeInput(attrs={
            'type': 'time',
            'class': 'form-control'
        })
    )
    saida = forms.TimeField(
        required=False,
        widget=forms.TimeInput(attrs={
            'type': 'time',
            'class': 'form-control'
        })
    )
    autorizado_por = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Nome da pessoa que autorizou',
            'class': 'form-control'
        })
    )
