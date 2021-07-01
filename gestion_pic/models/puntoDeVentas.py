from odoo import models, fields
class puntoDeVentas(models.Model):
    _name = 'gestion_pic.puntodeventas'
    idPuntoDeVentas = fields.Char('ID')
    codigo = fields.Char('Codigo')
    puntoDeVenta = fields.Char('Punto de Venta')
    domicilio = fields.Char('Domicilio')
    localidad = fields.Char('Localidad')
    tipoServicioAFIP = fields.Char('tipoServicioAFIP') #POSIBLE ENUM
    terminalCaptura = fields.Char('terminalCaptura')
    idComercio = fields.Many2one('gestion_pic.comercios','comercios')