# -*- coding: utf-8 -*-
from odoo import models, fields


class adquirentes(models.Model):
    _name = 'gestion_pic.adquirentes'

    idAdquirente = fields.Char('Id Adquirente')
    adquirente = fields.Char('Adquirente')