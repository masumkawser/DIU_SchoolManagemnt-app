# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'School',
    'version' : '1.5',
    'summary': 'School',
    'sequence': 10,
    'description': """
        School
    """,

    'website': 'https://www.odoo.com/app/invoicing',
    'images' : [],
    'depends' : [],
    'data': [
        #security
        "security/ir.model.access.csv",
        
        #views
        "views/student.xml",
        "views/teacher.xml",
        "views/course.xml",
        "views/section.xml",
        "views/registration.xml",

        #menu
        
        "views/menu.xml",


    ],
    'demo': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,

    'license': 'LGPL-3',
}
