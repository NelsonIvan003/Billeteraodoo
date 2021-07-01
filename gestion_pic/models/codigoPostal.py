# -*- coding: utf-8 -*-
from odoo import models, fields
class codigoPostal(models.Model):
    _name= 'gestion_pic.codigopostal'
    idCodigoPostal = fields.Char('ID')
    codigo = fields.Char('Codigo')
    localidad = fields.Char('Localidad')