from odoo import models, fields

class tipoTipoOperacion(models.Model):
    _name = 'analisis_pic.tipotipooperacion'
    idtipoTipoOperacion = fields.Char('ID')
    codigo = fields.Char('Codigo')
    descripcion = fields.Char('Descipción')
