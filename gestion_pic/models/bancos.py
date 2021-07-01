# -*- coding: utf-8 -*-
from odoo import models, fields

class bancos(models.Model):
    _name = 'gestion_pic.bancos'
    idBanco = fields.Char('Banco')
    banco = fields.Char('Banco Nombre')
    descripcion = fields.Char('Descripción')
    razonSocial = fields.Char('Razón Social')
    domicilio = fields.Char('Dirección')
    localidad = fields.Char('Localidad')
    telefono = fields.Char('Telefono')
    email = fields.Char('Email')