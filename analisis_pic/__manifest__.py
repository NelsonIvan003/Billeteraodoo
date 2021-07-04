# -*- coding: utf-8 -*-

{
    'name': 'Análisis PIC',
    'version': '1.0',
    'depends': ['base','gestion_pic'],
    'summary': """
    Negocios, Clientes,Zonas,Balance,Cupones,Servicios,Promociones,Informes
    """,
    'installable': True,
    'application': True,
    'auto_install': False,
    'data': [
            'views/analisis_pic.xml',
        ],
}
