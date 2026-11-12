from django import forms

from .models import TipoServico


class BuscaPrestadorForm(forms.Form):
    cidade = forms.CharField(
        required=False,
        label='Localização',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Digite a cidade ou bairro'}),
    )
    tipo_servico = forms.ModelChoiceField(
        required=False,
        label='Tipo de serviço',
        queryset=TipoServico.objects.none(),
        empty_label='Todos os serviços',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipo_servico'].queryset = TipoServico.objects.order_by('nome')
