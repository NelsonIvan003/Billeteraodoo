# -*- coding: utf-8 -*-
from odoo import models, fields
class contratoBancoComercio(models.Model):
    #_name = 'gestion_pic.contratoBancoComercio'
    _name = 'gestion_pic.contratobancocomercio'
    idBanco = fields.Many2many('gestion_pic.bancos','bancos')
    idComercio = fields.Many2many('gestion_pic.comercios','comercios')
    cuentaRecaudadora = fields.Char('cuenta_recaudadora (cbu, cvu)')
    beneficiario = fields.Char('beneficiario')
    sucursal = fields.Char('sucursal')
    tasa = fields.Float('tasa')
