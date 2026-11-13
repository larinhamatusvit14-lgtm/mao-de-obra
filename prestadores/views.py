from django.shortcuts import render

from .forms import BuscaPrestadorForm


def home(request):
    form = BuscaPrestadorForm(request.GET or None)
    prestadores = []
    mock_mode = True

    context = {
        'form': form,
        'prestadores': prestadores,
        'mock_mode': mock_mode,
    }
    return render(request, 'prestadores/index.html', context)
