# -*- coding: utf-8 -*-
from odoo import models, fields

class tickets(models.Model):
    _name = 'gestion_pic.tickets'
    idTickets = fields.Char('Id TicKet')
    detalleTicket = fields.Char('Detalle Ticket')
    idCliente = fields.Many2one('gestion_pic.clientes','clientes')
    fecha = fields.Date('Fecha')
    hora = fields.Datetime('Hora')

    idAdquirente = fields.Many2one('gestion_pic.adquirentes','adquirentes')
    domicilio = fields.Char('Direccion')
    nroComprobante = fields.Integer('Nro Comprobante')
    nroTerminal = fields.Integer('Nro Terminal')
    loteCargo = fields.Integer('Lote Cargo')
    aut = fields.Boolean('Autorizacion')
    planCuota = fields.Char('Plan Cuota')