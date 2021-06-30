# -*- coding: utf-8 -*-
from odoo import models, fields

class Operacion(models.Model):
    _name = 'gestion_pic.operacion'
    id_operacion = fields.Char('Id')
    """
       importe_total
    importe_impuestos
    id_tipo_operacion
    fecha
    hora
    id_cliente
    id_comercio
    id_tipo_negocio_operacion
    id_promocion
    id_linea_de_caja
    id_tipo_recarga
    id_medio_de_pago
    id_medio_de_cobro
    id_banco_emisor
    id_banco_pagador
    nro_operacion  
    CUANDO ME LEVANTO SIGO :) y EMPIEZO CON LAS VISTAS
    """
