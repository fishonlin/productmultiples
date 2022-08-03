

{
    'name': 'Product Multiples Barcodes',
    "version": "14.0.1.0.1",
    'author': 'K Developer',
    'installable': True,
    'images': ['static/description/main_banner1.png'],
    'summary': 'Allows to define multiple additional barcodes for products and to search products by additional barcodes and internal reference.',
    'depends': [
        'product',
        'sale',
        'purchase',
        'stock',
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/multiply_barcode_wizard.xml',
        'views/product_template_views.xml',
    ],
}
