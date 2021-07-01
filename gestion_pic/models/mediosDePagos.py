from odoo import models,fields
class mediosDePagos(models.Model):
    _name = 'gestion_pic.mediosdepago'
    idMediosDePago = fields.Char('Id')
    medioDePago = fields.Selection([('prepaga','prepaga'), ('tradicional','tradicional') , ('nuevo','nuevo')])