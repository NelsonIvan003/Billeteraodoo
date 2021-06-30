# -*- coding: utf-8 -*-
from odoo import models, fields
class Campana(models.Model):
    _name = 'gestion_pic.campana'
    id_campana = fields.Char('Id')
    codigo = fields.Char('Codigo')
    descipcion = fields.Char('Descipción')
    promociones = fields.Many2one('gestion_pic.promocion','Promocion')