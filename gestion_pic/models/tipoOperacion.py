# -*- coding: utf-8 -*-
from odoo import models, fields

class tipoOperacion(models.Model):
    _name = 'gestion_pic.tipooperacion'
    idTipoOperacion = fields.Char('Id')
    codigo = fields.Char('Codigo')
    operacion = fields.Char('Operacion ')
    idMedioDePago = fields.Many2many('gestion_pic.mediosdetago','mediosDePago')
    idTipoTipoOperacion = fields.Many2one('gestion_pic.tipotipooperacion','tipoTipoOperacion')
    descripcion = fields.Selection([('prepaga','prepaga'), ('tradicional','tradicional'),('nuevo','nuevo')])
    idMediosDePago = fields.Many2one('gestion_pic.medios_de_pago','Mediosdepagos')