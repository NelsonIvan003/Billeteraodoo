# -*- coding: utf-8 -*-
from odoo import models, fields

class comercios(models.Model):
    _name = 'gestion_pic.comercios'
    id_comercio = fields.Char('Comercio',required=True)
    codigo = fields.Char('Codigo',required=True)
    cuit = fields.Char('Cuit', required= True)
    direccion = fields.Char('Direccion',required=True)
    telefono = fields.Char('Teléfono',required=True)
    tipo = fields.Char('Tipo',required=True)
    sucursal = fields.Char('sucursal')
    idBancoPagador = fields.Many2many('gestion_pic.bancos','bancos')

