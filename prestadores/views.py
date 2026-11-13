import json
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
        latitude=-23.5505,
        longitude=-46.6333,
        foto='https://randomuser.me/api/portraits/men/32.jpg',
        avaliacoes=[
            {'nome': 'Marina', 'nota': 5, 'texto': 'Atendimento excelente e acabamento impecável.'},
            {'nome': 'Jorge', 'nota': 5, 'texto': 'Muito responsável e pontual.'},
            {'nome': 'Patrícia', 'nota': 4, 'texto': 'Recomendado para manutenção elétrica.'},
        ],
    ),
    SimpleNamespace(
        nome='Ana Paula Ribeiro',
        tipo_servico=SimpleNamespace(nome='Encanador', slug='encanador'),
        cidade='Rio de Janeiro',
        bairro='Copacabana',
        descricao='Reparo de encanamentos e instalação de chuveiros.',
        whatsapp='5521998877665',
        latitude=-22.9707,
        longitude=-43.1822,
        foto='https://randomuser.me/api/portraits/women/44.jpg',
        avaliacoes=[
            {'nome': 'Lucas', 'nota': 5, 'texto': 'Conserto rápido e bem explicado.'},
            {'nome': 'Renata', 'nota': 5, 'texto': 'Profissional muito atenciosa.'},
            {'nome': 'Tiago', 'nota': 4, 'texto': 'Excelente custo-benefício.'},
        ],
    ),
    SimpleNamespace(
        nome='Roberto Nunes',
        tipo_servico=SimpleNamespace(nome='Pedreiro', slug='pedreiro'),
        cidade='Belo Horizonte',
        bairro='Savassi',
        descricao='Reformas, acabamento e assentamento de pisos.',
        whatsapp='5531988776655',
        latitude=-19.9167,
        longitude=-43.9345,
        foto='https://randomuser.me/api/portraits/men/75.jpg',
        avaliacoes=[
            {'nome': 'Cecília', 'nota': 5, 'texto': 'Acabamento muito bom e equipe organizada.'},
            {'nome': 'Miguel', 'nota': 5, 'texto': 'Prestou serviço com cuidado e limpeza.'},
            {'nome': 'Sabrina', 'nota': 4, 'texto': 'Muito profissional.'},
        ],
    ),
    SimpleNamespace(
        nome='Lívia Santos',
        tipo_servico=SimpleNamespace(nome='Manicure', slug='manicure'),
        cidade='Salvador',
        bairro='Barra',
        descricao='Cuidados com unhas, esmaltação e estética.',
        whatsapp='5571991234567',
        latitude=-13.0100,
        longitude=-38.5320,
        foto='https://randomuser.me/api/portraits/women/68.jpg',
        avaliacoes=[
            {'nome': 'Amanda', 'nota': 5, 'texto': 'Ambiente agradável e trabalho impecável.'},
            {'nome': 'Luiz', 'nota': 5, 'texto': 'Muito capricho nos detalhes.'},
            {'nome': 'Helena', 'nota': 4, 'texto': 'Atendimento super cordial.'},
        ],
    ),
    SimpleNamespace(
        nome='Tiago Almeida',
        tipo_servico=SimpleNamespace(nome='Pintor', slug='pintor'),
        cidade='Curitiba',
        bairro='Centro Cívico',
        descricao='Pintura interna e externa com acabamento premium.',
        whatsapp='5541987654321',
        latitude=-25.4297,
        longitude=-49.2711,
        foto='https://randomuser.me/api/portraits/men/18.jpg',
        avaliacoes=[
            {'nome': 'Dani', 'nota': 5, 'texto': 'Pintura clean e acabamento premium.'},
            {'nome': 'Fernando', 'nota': 5, 'texto': 'Muito eficiente e organizado.'},
            {'nome': 'Mariana', 'nota': 4, 'texto': 'Excelente profissional.'},
        ],
    ),
    SimpleNamespace(
        nome='Fernanda Costa',
        tipo_servico=SimpleNamespace(nome='Eletricista', slug='eletricista'),
        cidade='São Paulo',
        bairro='Jardins',
        descricao='Instalações elétricas em imóveis e manutenção preventiva.',
        whatsapp='5511987654321',
        latitude=-23.5682,
        longitude=-46.6937,
        foto='https://randomuser.me/api/portraits/women/29.jpg',
        avaliacoes=[
            {'nome': 'Vitor', 'nota': 5, 'texto': 'Excelente diagnóstico e solução prática.'},
            {'nome': 'Isabela', 'nota': 5, 'texto': 'Profissional muito confiável.'},
            {'nome': 'Rafael', 'nota': 4, 'texto': 'Atendimento ótimo e bem detalhado.'},
        ],
    ),
    SimpleNamespace(
        nome='Marcos Silva',
        tipo_servico=SimpleNamespace(nome='Encanador', slug='encanador'),
        cidade='São Paulo',
        bairro='Pinheiros',
        descricao='Vazamentos, torneiras e instalação de sistemas hidráulicos.',
        whatsapp='5511976543210',
        latitude=-23.5614,
        longitude=-46.6976,
        foto='https://randomuser.me/api/portraits/men/52.jpg',
        avaliacoes=[
            {'nome': 'Luan', 'nota': 5, 'texto': 'Solução rápida e sem complicações.'},
            {'nome': 'André', 'nota': 4, 'texto': 'Muito bom no atendimento.'},
            {'nome': 'Nina', 'nota': 5, 'texto': 'Recomendo para instalações hidráulicas.'},
        ],
    ),
    SimpleNamespace(
        nome='Patrícia Gomes',
        tipo_servico=SimpleNamespace(nome='Manicure', slug='manicure'),
        cidade='Fortaleza',
        bairro='Meireles',
        descricao='Alongamento, design de unhas e estética para eventos.',
        whatsapp='5585987654321',
        latitude=-3.7319,
        longitude=-38.5267,
        foto='https://randomuser.me/api/portraits/women/56.jpg',
        avaliacoes=[
            {'nome': 'Felipe', 'nota': 5, 'texto': 'Trabalho impecável e muito caprichoso.'},
            {'nome': 'Tais', 'nota': 5, 'texto': 'Ficou lindo e a experiência foi ótima.'},
            {'nome': 'Bruna', 'nota': 4, 'texto': 'Atendimento agradável e pontual.'},
        ],
    ),
    SimpleNamespace(
        nome='Rafael Costa',
        tipo_servico=SimpleNamespace(nome='Pedreiro', slug='pedreiro'),
        cidade='Recife',
        bairro='Boa Viagem',
        descricao='Obras, reformas e acabamento de alto padrão.',
        whatsapp='5581987654321',
        latitude=-8.1366,
        longitude=-34.9156,
        foto='https://randomuser.me/api/portraits/men/84.jpg',
        avaliacoes=[
            {'nome': 'Elaine', 'nota': 5, 'texto': 'Reforma com muito cuidado e organização.'},
            {'nome': 'Paulo', 'nota': 5, 'texto': 'Muito bom no acabamento final.'},
            {'nome': 'Cássia', 'nota': 4, 'texto': 'Entrega dentro do prazo.'},
        ],
    ),
    SimpleNamespace(
        nome='Juliana Ferreira',
        tipo_servico=SimpleNamespace(nome='Pintor', slug='pintor'),
        cidade='Porto Alegre',
        bairro='Moinhos de Vento',
        descricao='Pintura residencial, acabamentos e revitalização de imóveis.',
        whatsapp='5551987654321',
        latitude=-30.0346,
        longitude=-51.2177,
        foto='https://randomuser.me/api/portraits/women/14.jpg',
        avaliacoes=[
            {'nome': 'Pedro', 'nota': 5, 'texto': 'Pintura muito elegante e bem feita.'},
            {'nome': 'Gislaine', 'nota': 5, 'texto': 'Fez a diferença no visual do imóvel.'},
            {'nome': 'Mateus', 'nota': 4, 'texto': 'Ponto de atenção no acabamento.'},
        ],
    ),
    SimpleNamespace(
        nome='Daniel Soares',
        tipo_servico=SimpleNamespace(nome='Eletricista', slug='eletricista'),
        cidade='Brasília',
        bairro='Asa Norte',
        descricao='Manutenção elétrica predial e instalações modernas.',
        whatsapp='5561987654321',
        latitude=-15.7801,
        longitude=-47.9292,
        foto='https://randomuser.me/api/portraits/men/62.jpg',
        avaliacoes=[
            {'nome': 'Clara', 'nota': 5, 'texto': 'Excelente diagnóstico e solução segura.'},
            {'nome': 'Eduardo', 'nota': 5, 'texto': 'Muito eficiente e confiável.'},
            {'nome': 'Rosa', 'nota': 4, 'texto': 'Atendimento profissional e claro.'},
        ],
    ),
    SimpleNamespace(
        nome='Beatriz Rocha',
        tipo_servico=SimpleNamespace(nome='Jardineiro', slug='jardineiro'),
        cidade='Porto Alegre',
        bairro='Cristal',
        descricao='Paisagismo, manutenção de jardins e poda ornamental.',
        whatsapp='5551998877665',
        latitude=-30.0344,
        longitude=-51.2274,
        foto='https://randomuser.me/api/portraits/women/65.jpg',
        avaliacoes=[
            {'nome': 'Júlio', 'nota': 5, 'texto': 'Jardim ficou lindo e bem cuidado.'},
            {'nome': 'Nara', 'nota': 5, 'texto': 'Excelente atenção aos detalhes.'},
            {'nome': 'João', 'nota': 4, 'texto': 'Profissional pontual e impecável.'},
        ],
    ),
    SimpleNamespace(
        nome='Leandro Martins',
        tipo_servico=SimpleNamespace(nome='Mecânico', slug='mecanico'),
        cidade='Recife',
        bairro='Casa Amarela',
        descricao='Manutenção automotiva, diagnóstico e revisão leve.',
        whatsapp='5581983322110',
        latitude=-8.0245,
        longitude=-34.9299,
        foto='https://randomuser.me/api/portraits/men/47.jpg',
        avaliacoes=[
            {'nome': 'Chico', 'nota': 5, 'texto': 'Diagnóstico preciso e muita honestidade.'},
            {'nome': 'Renata', 'nota': 5, 'texto': 'Carro saiu pronto e bem revisado.'},
            {'nome': 'Paula', 'nota': 4, 'texto': 'Ótimo custo-benefício.'},
        ],
    ),
    SimpleNamespace(
        nome='Sofia Dias',
        tipo_servico=SimpleNamespace(nome='Cabeleireiro', slug='cabeleireiro'),
        cidade='Salvador',
        bairro='Itapuã',
        descricao='Cortes, coloração, hidratação e estética capilar.',
        whatsapp='5571984567890',
        latitude=-13.0061,
        longitude=-38.5105,
        foto='https://randomuser.me/api/portraits/women/77.jpg',
        avaliacoes=[
            {'nome': 'Karla', 'nota': 5, 'texto': 'Atendimento top e corte impecável.'},
            {'nome': 'Lucas', 'nota': 5, 'texto': 'Muito profissional e cuidadosa.'},
            {'nome': 'Taís', 'nota': 4, 'texto': 'Ambiente agradável e capricho.'},
        ],
    ),
    SimpleNamespace(
        nome='Guilherme Prado',
        tipo_servico=SimpleNamespace(nome='Instalador de Ar Condicionado', slug='ar-condicionado'),
        cidade='Curitiba',
        bairro='Bigorrilho',
        descricao='Instalação, manutenção e limpeza de aparelhos de ar-condicionado.',
        whatsapp='5541981234567',
        latitude=-25.4195,
        longitude=-49.2710,
        foto='https://randomuser.me/api/portraits/men/13.jpg',
        avaliacoes=[
            {'nome': 'Marta', 'nota': 5, 'texto': 'Instalação rápida e muito bem feita.'},
            {'nome': 'Diego', 'nota': 5, 'texto': 'Boa explicação e serviço limpo.'},
            {'nome': 'Luiza', 'nota': 4, 'texto': 'Conseguiu resolver o problema sem complicar.'},
        ],
    ),
    SimpleNamespace(
        nome='Marina Alves',
        tipo_servico=SimpleNamespace(nome='Faxineiro', slug='faxineiro'),
        cidade='São Paulo',
        bairro='Moema',
        descricao='Limpeza residencial, organização e manutenção de ambientes.',
        whatsapp='5511987654422',
        latitude=-23.6033,
        longitude=-46.6627,
        foto='https://randomuser.me/api/portraits/women/31.jpg',
        avaliacoes=[
            {'nome': 'Aline', 'nota': 5, 'texto': 'Casa impecável e muito bem organizada.'},
            {'nome': 'Otávio', 'nota': 5, 'texto': 'Atendimento pontual e profissional.'},
            {'nome': 'Diana', 'nota': 4, 'texto': 'Muito eficiente.'},
        ],
    ),
    SimpleNamespace(
        nome='Henrique Souza',
        tipo_servico=SimpleNamespace(nome='Montador de Móveis', slug='montador'),
        cidade='Rio de Janeiro',
        bairro='Tijuca',
        descricao='Montagem de móveis, armários e itens de decoração.',
        whatsapp='5521997766554',
        latitude=-22.9239,
        longitude=-43.2328,
        foto='https://randomuser.me/api/portraits/men/90.jpg',
        avaliacoes=[
            {'nome': 'Fábio', 'nota': 5, 'texto': 'Montagem rápida e perfeita.'},
            {'nome': 'Lívia', 'nota': 5, 'texto': 'Ótima organização e acabamento.'},
            {'nome': 'César', 'nota': 4, 'texto': 'Muito confiável.'},
        ],
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

    prestadores_json = json.dumps([
        {
            'nome': p.nome,
            'tipo': p.tipo_servico.nome,
            'cidade': p.cidade,
            'bairro': p.bairro,
            'descricao': p.descricao,
            'foto': getattr(p, 'foto', ''),
            'whatsapp': p.whatsapp,
            'latitude': p.latitude,
            'longitude': p.longitude,
            'avaliacoes': getattr(p, 'avaliacoes', []),
        }
        for p in prestadores
    ])

    context = {
        'form': form,
        'prestadores': prestadores,
        'prestadores_json': prestadores_json,
        'mock_mode': mock_mode,
    }
    return render(request, 'prestadores/index.html', context)
