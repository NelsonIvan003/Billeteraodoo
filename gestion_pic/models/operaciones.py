# -*- coding: utf-8 -*-
from odoo import models, fields

class operaciones(models.Model):
    _name = 'gestion_pic.operaciones'
    idOperacion = fields.Char('Id')
    numeroOpracion = fields.Char('Nro')
    operacion = fields.Selection([('recarga','recarga'), ('compra','compra')])
    importeTotal = fields.Float('Total')
    importeImpuesto = fields.Float('Impuesto')
    idTipoOperacion = fields.Many2one('gestion_pic.tipoOperacion','tipoOperacion')
    fecha = fields.Date('Fecha')
    hora = fields.Datetime('Hora')
    idCliente = fields.Many2one('gestion_pic.clientes','clientes')
    idComercio = fields.Many2one('gestion_pic.comercios','comercios')
    #idTipoNegocioOperacion
    idPromocion = fields.Many2one('gestion_pic.promociones','promociones')
    idPuntoDeVenta = fields.Many2one('gestion_pic.puntoDeVentas','puntoDeVentas')
    idTiporecarga = fields.Char('Tipo Recarga') #Preguntar
    idMedioPago = fields.Many2one('gestion_pic.mediosDePago','mediosDePago')
    idMediodDeCobro = fields.Many2one('gestion_pic.mediosDePago', 'mediosDePago')
    idBancoEmisor = fields.Many2one('gestion_pic.bancos', 'bancos')
    idBancoPagador = fields.Many2one('gestion_pic.bancos', 'bancos')
    estadoOperacion = fields.Selection([('rechazada','rechazada'),('aprobada','aprobada'),('por aprobar','por aprobar')]) #para mi va una enum hombre
    motivoOperación = fields.Char('Motivo de operacion')
    idCuponesVendidos = fields.Many2one('gestion_pic.cupones', 'cupones')
