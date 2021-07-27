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
        "account",
        "sale",
        "purchase"
    ],
    # always loaded
    'data': [
        'invoice/ti_custom_invoice.xml',
        'sale_order/ti_custom_sale_order.xml',
        'purchase_order/ti_custom_purchase_order.xml',
        'purchase_order/ti_custom_rfq.xml'
    ]
}
