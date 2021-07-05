# -*- coding: utf-8 -*-
from odoo import models, fields

class billeteras(models.Model):
    _name = 'gestion_pic.billeteras'
    idBilletera = fields.Char('idBilletera')
    codigoBilletera = fields.Char('Codigo Billetera')
    nombreBilletera = fields.Char('Nombre Billetera')
    idCliente = fields.Many2one('gestion_pic.clientes','clientes')
    idComercio = fields.Many2many('gestion_pic.comercios','comercios')
    idMediosDePagoAsociados = fields.Many2one('gestion_pic.mediosdepago', 'mediosdepago')
    idOperacion = fields.Many2one('analisis_pic.operaciones', 'operaciones')
    estadoBilletera = fields.Char('Estado')
    fechaAlta = fields.Date('Fecha Alta')
    codigoSeguridad = fields.Char('Codigo Seguridad')
    huellaAsociada = fields.Char('Huella Asociada')
    rostroAsociado = fields.Char('Rostro Asociado')
    saldo = fields.Char('Saldo')
    creditoMaximo = fields.Float('Credito Maximo')
