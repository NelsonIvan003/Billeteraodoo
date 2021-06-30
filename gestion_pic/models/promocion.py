# -*- coding: utf-8 -*-
from odoo import models, fields

class Promocion(models.Model):
    _name = 'gestion_pic.promocion'
    id_promocion = fields.Char('Id')