from odoo import models,fields

class localidades(models.Model):
    _name = 'gestion_pic.localidades'
    idLocalidad = fields.Char('ID')
    codigo = fields.Char('Descripción')
    localidad = fields.Char('Localidad')
    zona = fields.Char('Zona')
    codigoPostal = fields.Many2one('gestion_pic.codigoPostal','codigoPostal')
    provincia = fields.Char('Provincia')
    pais = fields.Char('Pais')
    geo = fields.Char('Geo')