# -*- coding: utf-8 -*-
from odoo import models, fields
class Localidadcodigopostal(models.Model):
    _name= 'gestion_pic.localidad_codigo_postal'
    id_locacion_codigo_postal = fields.Char('Id codigo postal')
    codigo = fields.Char('Codigo')
    descripcion = fields.Char('Descripción')