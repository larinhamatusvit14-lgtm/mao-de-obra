from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='TipoServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80, unique=True, verbose_name='Tipo de serviço')),
                ('descricao', models.TextField(blank=True, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'tipo de serviço',
                'verbose_name_plural': 'tipos de serviço',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Prestador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome completo')),
                ('cidade', models.CharField(max_length=100, verbose_name='Cidade')),
                ('bairro', models.CharField(max_length=100, verbose_name='Bairro')),
                ('descricao', models.TextField(verbose_name='Descrição dos serviços')),
                ('telefone', models.CharField(max_length=20, verbose_name='Telefone')),
                ('whatsapp', models.CharField(max_length=20, verbose_name='WhatsApp')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('tipo_servico', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='prestadores', to='prestadores.tiposervico', verbose_name='Tipo de serviço')),
            ],
            options={
                'verbose_name': 'prestador',
                'verbose_name_plural': 'prestadores',
                'ordering': ['cidade', 'bairro', 'nome'],
            },
        ),
    ]
