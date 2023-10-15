# noinspection PyStatementEffect
{
    'name': "Area Based Price",
    'sequence': 50,

    'summary': """
        Calculates product prices based on their area""",

    'author': "Arxi",
    'website': "http://www.arxi.pt",

    'category': 'Sales',
    'version': '13.0.1.0.10',
    'license': 'OPL-1',

    'price': 45.00,
    'currency': 'EUR',

    'depends': ['E3K_so_po_url', 'sale', 'account'],

    'data': [
    	'views/product_views.xml',
        'views/sale_order_view.xml',
        'views/purchase_order_view.xml',
        'views/account_invoice_views.xml',
        'views/res_company_view.xml',
        'report/report_sale.xml',
        'report/report_purchase.xml',
        'report/report_invoice.xml',
        #'report/purchase_quotation_templates.xml',
        #'report/purchase_order_templates.xml',
    ],

    'images': [
        'static/demo.gif',
        'static/description/banner.png',
    ],
}
