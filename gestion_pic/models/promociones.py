# -*- coding: utf-8 -*-
from odoo import models, fields

class promociones(models.Model):
    _name = 'gestion_pic.promociones'

    idPromocion = fields.Char('Id')
    promocion = fields.Char('Promocion')
    idComercio = fields.Many2many('gestion_pic.comercios', 'comercios')
    porcentajeDescuento = fields.Float('Descuento')
    piezaPublicitariaTexto = fields.Char('Publicitaria Texto')
    piezaPublicitariaImagen = fields.Char('Publicitaria Imagen')
    porcentajeAporteComercio = fields.Float('Porcentaje Aporte de Comercio')
    porcentajeAporteAderente = fields.Float('Porcentaje Aderente')
    porcentajeAporteBanco = fields.Float('Aporte Banco')
    fechaInicio = fields.Date('Fecha Inicio')
    horaInicio = fields.Datetime('Hora Inicio')
    fechaFin = fields.Date('Fecha Fin')
    horaFin = fields.Datetime('Hora Fin')
    estado = fields.Boolean('Estado')
    #armar caso de uso
    #listado de promociones
    #crear promocion




