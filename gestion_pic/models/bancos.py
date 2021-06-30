# -*- coding: utf-8 -*-
from odoo import models, fields

class Banco(models.Model):
    _name = 'configuracion_pic.banco'
    id_banco = fields.Char('Banco')
    codigo = fields.Char('Codigo')
    descripcion = fields.Char('Descripción')