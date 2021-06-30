from odoo import models, fields
class Lineacaja(models.Model):
    _name = 'gestion_pic.linea_caja'
    id_linea_caja = fields.Char('Id linea de caja')
    codigo = fields.Char('Codigo')
    descripcion = fields.Char('Descripcion')
    id_locación = fields.Many2one('gestion_pic.comercio','Comercio')