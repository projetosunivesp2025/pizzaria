from django.contrib import admin
from django.utils.html import format_html, mark_safe
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from django import forms
from django.contrib.auth.models import User
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponseRedirect

class PedidoAdmin(admin.ModelAdmin):
    def obter_urls(self):
        pass

    def alterar_endereco(self, request, queryset):
        if queryset.count() != 1:
            self.message_user(request, "Por favor, selecione apenas um pedido para alterar o endereço.", level=messages.WARNING)
            return
        
        pedido = queryset.first()
        return HttpResponseRedirect(f"/.../?pedido_id={pedido.numero}")
    alterar_endereco.short_description = "Alterar Endereço do Pedido"

    
    def obter_status_colorido(self, obj):
        cores_status = {
            'PENDENTE': '#FFC107',
            'EM_PREPARO': '#FF9800',
            'EM_ENTREGA': 'linear-gradient(to right, #28a745 50%, #5cb85c 50%)',
            'ENTREGUE': '#28a745',
            'CANCELADO': '#6c757d'
        }
        status_display = dict(Pedido.STATUS_CHOICES).get(obj.status, obj.status)
        if obj.status == 'EM_ENTREGA':
            return format_html('<span style="padding: 3px 8px; border-radius: 10px; display: inline-block; background: {}; color: white;">{}</span>', cores_status[obj.status], status_display)
        else:
            return format_html('<span style="padding: 3px 8px; border-radius: 10px; display: inline-block; background-color: {}; color: white;">{}</span>', cores_status[obj.status], status_display)
    obter_status_colorido.short_description = 'Status'


class EntregadorAdmin(admin.ModelAdmin):
    def obter_formulario(self, request, obj=None, **kwargs):
        kwargs.pop('fields', None)
        
        formulario = super().get_form(request, obj, **kwargs)
        
        formulario.base_fields['nome'].required = True
        formulario.base_fields['telefone'].required = True
        formulario.base_fields['user'].required = True
        
        formulario.base_fields['nome'].help_text = "Digite o nome completo do entregador (obrigatório)"
        formulario.base_fields['telefone'].help_text = "Digite o número do telefone com DDD, ex: (14) 99999-9999 (obrigatório)"
        formulario.base_fields['user'].help_text = "Selecione um usuário do sistema para associar a este entregador. Importante: Cada entregador deve ter um usuário único (obrigatório)"
        formulario.base_fields['disponivel'].help_text = "Marque esta opção se o entregador está disponível para receber pedidos"
        
        return formulario

class ParadaEntregadorAdmin(admin.ModelAdmin):
    def visualizar_lista_alteracao(self, request, extra_context=None):
        pass

    def obter_numero_pedido(self, obj):
        pass
    
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Entregador, EntregadorAdmin)
admin.site.register(ParadaEntregador, ParadaEntregadorAdmin)