# -*- coding: utf-8 -*-
from odoo import models, fields

class clientes(models.Model):
    _name = 'gestion_pic.clientes'
    idCliente = fields.Char('Id')
    codigo = fields.Char('codigo')
    apellido = fields.Char('Apellido')
    nombre = fields.Char('Nombre')
    huella = fields.Char('Huella')
    domicilio = fields.Char('Dirección')
    localidad = fields.Char('Localidad')
    dni = fields.Char('Dni')
    cbu = fields.Char('Cbu')
    cvu = fields.Char('Cvu')
    fechaNacimiento = fields.Date('Fecha de Nacimiento')
    telefono = fields.Char('Telefono')
    email = fields.Char('Email')
    facebook = fields.Char('Facebook')
    instagram = fields.Char('Instagram')
    sexo = fields.Selection([('masculino','Masculino'),('femenino','Femenino')]) #para mi va una enum hombre
    genero = fields.Char('Genero')
