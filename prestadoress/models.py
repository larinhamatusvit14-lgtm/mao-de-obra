from django.db import models


class TipoServico(models.Model):
    nome = models.CharField(max_length=80, unique=True, verbose_name='Tipo de serviço')
    descricao = models.TextField(blank=True, verbose_name='Descrição')

    class Meta:
        verbose_name = 'tipo de serviço'
        verbose_name_plural = 'tipos de serviço'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Prestador(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Nome completo')
    tipo_servico = models.ForeignKey(
        TipoServico,
        on_delete=models.PROTECT,
        related_name='prestadores',
        verbose_name='Tipo de serviço',
    )
    cidade = models.CharField(max_length=100, verbose_name='Cidade')
    bairro = models.CharField(max_length=100, verbose_name='Bairro')
    descricao = models.TextField(verbose_name='Descrição dos serviços')
    telefone = models.CharField(max_length=20, verbose_name='Telefone')
    whatsapp = models.CharField(max_length=20, verbose_name='WhatsApp')
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['cidade', 'bairro', 'nome']
        verbose_name = 'prestador'
        verbose_name_plural = 'prestadores'

    def __str__(self):
        return self.nome

    @property
    def localizacao(self):
        return f'{self.bairro} - {self.cidade}'
