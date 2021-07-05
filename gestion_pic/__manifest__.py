# -*- coding: utf-8 -*-


{
    'name': 'Gestion PIC',
    'version': '1.0',
    'depends': ['base'],
    'summary': """Gestión de Comercios,
        Gestión Bancos,  
        Gestión de Adquirentes, 
        Gestión de Clientes, 
        Gestión de Cupones, 
        Contratos, 
        Adelantamientos, 
        Gestión de Promociones
    """,
    'installable': True,
    'application': True,
    'auto_install': False,
    'data': [
            'views/gestion_pic.xml',
            'views/promociones/promociones.xml',
            'views/comercios/comercios.xml',
            'views/bancos/bancos.xml',
            'views/adquirentes/adquirentes.xml',
            'views/clientes/clientes.xml',
            'views/cupones/cupones.xml',
            'views/contratos/contratos.xml',
            'views/adelantamientos/adelantamientos.xml',
        ],
}