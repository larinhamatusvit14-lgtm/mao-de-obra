# Administração temporariamente desativada enquanto o PostgreSQL não estiver pronto.
# from django.contrib import admin
#
# from .models import Prestador, TipoServico
#
#
# @admin.register(TipoServico)
# class TipoServicoAdmin(admin.ModelAdmin):
#     list_display = ('nome',)
#     search_fields = ('nome',)
#
#
# @admin.register(Prestador)
# class PrestadorAdmin(admin.ModelAdmin):
#     list_display = ('nome', 'tipo_servico', 'cidade', 'bairro', 'telefone', 'whatsapp')
#     list_filter = ('tipo_servico', 'cidade')
#     search_fields = ('nome', 'cidade', 'bairro', 'telefone', 'whatsapp')
