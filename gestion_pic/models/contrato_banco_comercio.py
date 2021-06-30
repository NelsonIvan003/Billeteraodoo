# -*- coding: utf-8 -*-
from odoo import models, fields
class Contratobancocomercio(models.Model):
    _name = 'configuracion_pic.contrato_banco_comercio'
    id_banco =  fields.Many2many('configuracion_pic.banco','Banco')
    id_comercio = fields.Many2many('configuracion_pic.comercio','Comercio')