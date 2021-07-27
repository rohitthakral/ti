# -*- coding: utf-8 -*-
{
    'name': "TI Report Templates",
    'summary': "Customized Report Templates",
    'author': "Target Integration",
    'website': "http://www.targetintegration.com",
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        "account"
    ],
    # always loaded
    'data': [
        'invoice/ti_custom_invoice.xml'
    ]
}
