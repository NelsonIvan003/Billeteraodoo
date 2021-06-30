# -*- coding: utf-8 -*-
from odoo import models, fields

class Clientes(models.Model):
    _name = 'gestion_pic.cliente'
    id_cliente = fields.Char('Id')
    nombre = fields.Char('Nombre')
    apellido = fields.Char('Apellido')
    sexo = fields.Selection(['Masculino','Femenino']) #para mi va una enum hombre
    huella = fields.Char('Huella')
    dni = fields.Char('Dni')
    fecha_nacimiento = fields.Date('Fecha de Nacimiento')
    pais = fields.Char('Pais')
    provincia = fields.Char('Provincia')
    localidad = fields.Char('Localidad')
    direccion = fields.Char('Dirección')
    codigo_postal = fields.Char('Codigo  Postal') #https://es.youbianku.com/Argentina
    cbu = fields.Char('Cbu')
    cvu = fields.Char('Cvu')
    cuit_cuil = fields.Char('Cuit/Cuil')
    mail = fields.Char('Mail')
    nro_telefono = fields.Char('Telefono')