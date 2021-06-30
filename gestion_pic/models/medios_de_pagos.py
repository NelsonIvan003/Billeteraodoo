from odoo import models,fields
class Mediosdepagos(models.Model):
    _name = 'gestion_pic.medios_de_pago'
    id_medios_de_pagos = fields.Char('Id')
    descripcion = fields.Selection(['prepaga', 'tradicional', 'nuevo'])