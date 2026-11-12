from django.test import TestCase

from .models import Prestador, TipoServico


class PrestadorFilterTests(TestCase):
    def setUp(self):
        self.eletricista = TipoServico.objects.create(nome='Eletricista')
        self.encanador = TipoServico.objects.create(nome='Encanador')

        Prestador.objects.create(
            nome='João Silva',
            tipo_servico=self.eletricista,
            cidade='São Paulo',
            bairro='Centro',
            descricao='Instalações elétricas residenciais.',
            telefone='11999990000',
            whatsapp='11999990000',
        )
        Prestador.objects.create(
            nome='Maria Souza',
            tipo_servico=self.encanador,
            cidade='Rio de Janeiro',
            bairro='Copacabana',
            descricao='Reparo de vazamentos e encanamentos.',
            telefone='21999991111',
            whatsapp='21999991111',
        )

    def test_filtra_por_cidade_e_tipo_de_servico(self):
        resultados = Prestador.objects.filter(cidade='São Paulo', tipo_servico__nome='Eletricista')
        self.assertEqual(resultados.count(), 1)
        self.assertEqual(resultados.first().nome, 'João Silva')

    def test_filtra_por_tipo_de_servico(self):
        resultados = Prestador.objects.filter(tipo_servico__nome='Encanador')
        self.assertEqual(resultados.count(), 1)
        self.assertEqual(resultados.first().nome, 'Maria Souza')
