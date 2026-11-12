from django.shortcuts import render

from .forms import BuscaPrestadorForm
from .models import Prestador


def home(request):
    form = BuscaPrestadorForm(request.GET or None)

    prestadores = Prestador.objects.select_related('tipo_servico').all()

    if form.is_valid():
        cidade = form.cleaned_data.get('cidade') or ''
        tipo_servico = form.cleaned_data.get('tipo_servico')

        if cidade:
            prestadores = prestadores.filter(cidade__icontains=cidade) | prestadores.filter(
                bairro__icontains=cidade
            )

        if tipo_servico:
            prestadores = prestadores.filter(tipo_servico=tipo_servico)

    context = {
        'form': form,
        'prestadores': prestadores.order_by('cidade', 'bairro', 'nome'),
    }
    return render(request, 'prestadores/index.html', context)
