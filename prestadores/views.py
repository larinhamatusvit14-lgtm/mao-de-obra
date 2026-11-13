from types import SimpleNamespace

from django.shortcuts import render

from .forms import BuscaPrestadorForm


MOCK_PRESTADORES = [
    SimpleNamespace(
        nome='Carlos Mendes',
        tipo_servico=SimpleNamespace(nome='Eletricista', slug='eletricista'),
        cidade='São Paulo',
        bairro='Centro',
        descricao='Instalações elétricas, quadros e manutenção residencial.',
        whatsapp='5511998765432',
    ),
    SimpleNamespace(
        nome='Ana Paula Ribeiro',
        tipo_servico=SimpleNamespace(nome='Encanador', slug='encanador'),
        cidade='Rio de Janeiro',
        bairro='Copacabana',
        descricao='Reparo de encanamentos e instalação de chuveiros.',
        whatsapp='5521998877665',
    ),
    SimpleNamespace(
        nome='Roberto Nunes',
        tipo_servico=SimpleNamespace(nome='Pedreiro', slug='pedreiro'),
        cidade='Belo Horizonte',
        bairro='Savassi',
        descricao='Reformas, acabamento e assentamento de pisos.',
        whatsapp='5531988776655',
    ),
    SimpleNamespace(
        nome='Lívia Santos',
        tipo_servico=SimpleNamespace(nome='Manicure', slug='manicure'),
        cidade='Salvador',
        bairro='Barra',
        descricao='Cuidados com unhas, esmaltação e estética.',
        whatsapp='5571991234567',
    ),
    SimpleNamespace(
        nome='Tiago Almeida',
        tipo_servico=SimpleNamespace(nome='Pintor', slug='pintor'),
        cidade='Curitiba',
        bairro='Centro Cívico',
        descricao='Pintura interna e externa com acabamento premium.',
        whatsapp='5541987654321',
    ),
    SimpleNamespace(
        nome='Fernanda Costa',
        tipo_servico=SimpleNamespace(nome='Eletricista', slug='eletricista'),
        cidade='São Paulo',
        bairro='Jardins',
        descricao='Instalações elétricas em imóveis e manutenção preventiva.',
        whatsapp='5511987654321',
    ),
    SimpleNamespace(
        nome='Marcos Silva',
        tipo_servico=SimpleNamespace(nome='Encanador', slug='encanador'),
        cidade='São Paulo',
        bairro='Pinheiros',
        descricao='Vazamentos, torneiras e instalação de sistemas hidráulicos.',
        whatsapp='5511976543210',
    ),
]


def home(request):
    form = BuscaPrestadorForm(request.GET or None)
    prestadores = MOCK_PRESTADORES
    mock_mode = True

    if form.is_valid():
        cidade = (form.cleaned_data.get('cidade') or '').strip().lower()
        tipo_servico = form.cleaned_data.get('tipo_servico') or ''

        if cidade:
            prestadores = [
                p for p in prestadores
                if cidade in p.cidade.lower() or cidade in p.bairro.lower()
            ]

        if tipo_servico:
            prestadores = [
                p for p in prestadores if p.tipo_servico.slug == tipo_servico
            ]

    context = {
        'form': form,
        'prestadores': prestadores,
        'mock_mode': mock_mode,
    }
    return render(request, 'prestadores/index.html', context)
