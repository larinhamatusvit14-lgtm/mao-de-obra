from django.core.management.base import BaseCommand

from prestadores.models import Prestador, TipoServico


class Command(BaseCommand):
    help = 'Popula o banco com prestadores de exemplo para o Mão de Obra.'

    def handle(self, *args, **options):
        tipos = {
            'Eletricista': 'Instalações elétricas e manutenção residencial.',
            'Encanador': 'Reparo de encanamentos e vazamentos.',
            'Pedreiro': 'Construção, reforma e acabamento.',
            'Manicure': 'Cuidados com unhas e estética.',
            'Pintor': 'Pintura residencial e comercial.',
        }

        for nome, descricao in tipos.items():
            TipoServico.objects.get_or_create(nome=nome, defaults={'descricao': descricao})

        dados = [
            {
                'nome': 'Carlos Mendes',
                'tipo_servico': 'Eletricista',
                'cidade': 'São Paulo',
                'bairro': 'Centro',
                'descricao': 'Instalação elétrica residencial, quadros e manutenção preventiva.',
                'telefone': '11987654321',
                'whatsapp': '11987654321',
            },
            {
                'nome': 'Ana Paula Ribeiro',
                'tipo_servico': 'Encanador',
                'cidade': 'Rio de Janeiro',
                'bairro': 'Copacabana',
                'descricao': 'Vazamentos, troca de encanamento e manutenção de chuveiros.',
                'telefone': '21999887766',
                'whatsapp': '21999887766',
            },
            {
                'nome': 'Roberto Nunes',
                'tipo_servico': 'Pedreiro',
                'cidade': 'Belo Horizonte',
                'bairro': 'Savassi',
                'descricao': 'Reformas, assentamento de piso e acabamento de paredes.',
                'telefone': '31988776655',
                'whatsapp': '31988776655',
            },
            {
                'nome': 'Lívia Santos',
                'tipo_servico': 'Manicure',
                'cidade': 'Salvador',
                'bairro': 'Barra',
                'descricao': 'Alongamento, esmaltação e cuidado geral com unhas.',
                'telefone': '71991234567',
                'whatsapp': '71991234567',
            },
            {
                'nome': 'Tiago Almeida',
                'tipo_servico': 'Pintor',
                'cidade': 'Curitiba',
                'bairro': 'Centro Cívico',
                'descricao': 'Pintura interna e externa, preparação de superfícies e acabamento.',
                'telefone': '41988765432',
                'whatsapp': '41988765432',
            },
        ]

        for item in dados:
            tipo = TipoServico.objects.get(nome=item['tipo_servico'])
            Prestador.objects.get_or_create(
                nome=item['nome'],
                defaults={
                    'tipo_servico': tipo,
                    'cidade': item['cidade'],
                    'bairro': item['bairro'],
                    'descricao': item['descricao'],
                    'telefone': item['telefone'],
                    'whatsapp': item['whatsapp'],
                },
            )

        self.stdout.write(self.style.SUCCESS('Seed de prestadores criado com sucesso.'))
