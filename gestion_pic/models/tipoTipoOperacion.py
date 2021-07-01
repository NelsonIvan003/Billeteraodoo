from odoo import models, fields

class tipoTipoOperacion(models.Model):
    _name = 'gestion_pic.tipoTipoOperacion'
    idtipoTipoOperacion = fields.Char('ID')
    codigo = fields.Char('Codigo')
    descripcion = fields.Char('Descipción')
