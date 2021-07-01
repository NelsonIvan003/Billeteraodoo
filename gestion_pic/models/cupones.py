# -*- coding: utf-8 -*-
from odoo import models, fields

class cupones(models.Model):
    _name = 'gestion_pic.cupones'
    idCupon = fields.Char('Id Cupon')
    detalleCompra = fields.Char('Detalle Compra')
    idComercio = fields.Many2one('gestion_pic.comercios', 'comercios')
    idBanco = fields.Many2one('gestion_pic.bancos', 'bancos')
    importeTotal = fields.Float('Total')
    importeImpuesto = fields.Float('Impuesto')
    fechaVenta = fields.Date('Fecha Venta')
    fechaCompra = fields.Date('Fecha Compra')
    idDuenio = fields.Char('Dueño') # con cual hago clave foranea
