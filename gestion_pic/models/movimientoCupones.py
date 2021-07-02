from odoo import models, fields

class movimientoCupones(models.Model):
    _name = 'gestion_pic.movimientoscupones'
    idMovimientoCupon = fields.Char('ID')
    detalleMovimiento = fields.Char('Detalle')
    idBanco = fields.Many2one('gestion_pic.bancos', 'bancos')
    idComercio = fields.Many2one('gestion_pic.comercios', 'comercios')
    fecha = fields.Date('Fecha')
    hora = fields.Datetime('Hora')
    idOperacion = fields.Many2one('analisis_pic.operaciones', 'operaciones')
    importeImpuesto = fields.Float('Importe Impuesto')
    fechaVenta = fields.Date('Fecha Venta')
    fechaCobro = fields.Date('Fecha Compra')
    idBacoNuevoDuenio = fields.Many2one('gestion_pic.bancos', 'bancos')
    importeAdelantamiento = fields.Float('Adelantamiento')
    tasaDelAdelantamiento = fields.Float('Tasa Adelantamiento')
    idcupon = fields.Many2one('gestion_pic.cupones', 'cupones')


