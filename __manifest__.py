# -*- coding: utf-8 -*-
{
        'name': "Mrp worksheet based on sale order",
        'summary': """
        Provides raport showing all manufacturing elements related to source Sale Order
        Can be used as a working order in manufacturing plan""",

        'description': """ 
        desc:
        Provides raport showing all manufacturing elements related to source Sale Order
        Can be used as a working order in manufacturing plan""",

        'author': "Maciej Stawicki",
        'website': "http://odoo.3lance.pl",

        'category': 'Manufacturing','Sale'
        'version': '0.2',

        # any module necessary for this one to work correctly
        'depends': ['sale_mrp'],

        'license': 'AGPL-3',
        'data': [
            'reports/report_saleorder_worksheet.xml'
            ],
        'demo': [
            ],

        'installable': True,
        'auto_install': False,
        }
