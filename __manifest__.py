# -*- coding: utf-8 -*-
{
    'name': "Mrp worksheet based on sale order",

    'summary': """
        Provides raport showing all manufacturing elements related to source Sale Order
        Can be used as a working order in manufacturing plan""",

    'description': """
        Long description of module's purpose, 
        It depends
    """,

    'author': "Maciej Stawicki",
    'website': "http://3lance.pl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Manufacturing',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale_mrp'],

    'license': 'AGPL-3',
    # always loaded
    'data': [
        'reports/report_so_worksheet.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
    ],

    'installable': True,
    'auto_install': False,
}
