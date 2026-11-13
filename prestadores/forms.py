from django import forms


class BuscaPrestadorForm(forms.Form):
    cidade = forms.CharField(
        required=False,
        label='Localização',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Digite a cidade ou bairro'}),
    )
    tipo_servico = forms.ChoiceField(
        required=False,
        label='Tipo de serviço',
        choices=[
            ('', 'Todos os serviços'),
            ('eletricista', 'Eletricista'),
            ('encanador', 'Encanador'),
            ('pedreiro', 'Pedreiro'),
            ('manicure', 'Manicure'),
            ('pintor', 'Pintor'),
        ],
        widget=forms.Select(),
    )
