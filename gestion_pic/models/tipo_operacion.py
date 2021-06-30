# -*- coding: utf-8 -*-
from odoo import models, fields

class Tipooperacion(models.Model):
    _name = 'gestion_pic.tipo_operacion'
    id_tipo_operacion = fields.Char('Id')
    codigo = fields.Char('Codigo')
    descripcion = fields.Selection(['prepaga', 'tradicional', 'nuevo'])
    id_medios_de_pago = fields.Many2one('gestion_pic.medios_de_pago','Mediosdepagos')