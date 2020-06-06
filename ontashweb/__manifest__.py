# -*- coding: utf-8 -*-
{
    'name': "ontashweb",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Ontash",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',

        'views/home.xml',     
        'views/about.xml',
        'views/healthcare.xml',
        'views/government.xml',
        'views/products.xml',
        'views/contact.xml', 
        'views/enterprise.xml', 
        'views/mobility.xml',
        'views/cloud.xml',  
        'views/tour.xml' ,
        'views/demo.xml' ,   
        'views/odoo_videos.xml' , 
        'views/odoo_comparisons.xml' ,  
        'views/thankyou.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}