from odoo import models,fields

class Locacion(models.Model):
    _name = 'gestion_pic.locacion'
    id_locacion = fields.Char('Id locación')
    codigo = fields.Char('Descripción')
    zona = fields.Char('Zona')
    id_locacion_codigo_postal = fields.Many2one('gestion_pic.localidad_codigo_postal','Localidadcodigopostal')
    provincia = fields.Char('Provincia')
    pais = fields.Char('Pais')