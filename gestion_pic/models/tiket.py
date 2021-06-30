# -*- coding: utf-8 -*-
from odoo import models, fields

class Tiket(models.Model):
    _name = 'gestion_pic.tiket'
    empresa_razonSocial = fields.Char('Empresa/Razon Social')
    cuit_empresa =  fields.Char('Cuit Empresa')
    situacion_fiscal = fields.Char('situacion_fiscal')
    fecha = fields.Date('Fecha')
    hora = fields.Datetime('Hora')
    adquirente = fields.Char('Adquirente') #DUDA LINK A MEDIOS DE PAGOS? o STRING
    comercio_sucursal = fields.Char('Comercio/Sucursal')
    sucursal_domicilio = fields.Char('Sucursal Domicilio')
    nro_comprobante = fields.Integer('Nro Comprobante')
    nro_terminal = fields.Integer('Nro Terminal')
    tipo_operacion = fields.Selection(['com','rec','dev'])
    lote_cargo = fields.Integer('Lote')
    nro_cuenta_cliente = fields.Char('nro_cuenta_cliente') #CBU? o ID INTERNO
    importe_total = fields.Float('Total')
    plan_cuota11 = fields.Char('plan_cuota11')
    Autorizacion = fields.Boolean('Autorizacion')
