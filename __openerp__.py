# -*- coding: utf-8 -*-
{
    'name': "bp_8_0_social_media_for_res_partner",

    'summary': """
    social media links for the res_parter modul""",

    'description': """
    social media links for the res_parter modul""",

    'author': "BLOOPARK SYSTEMS GMBH. & CO. KG",
    'website': "http://www.bloopark.de",

    'category': 'social_media',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'hr'
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/res_partner_viev.xml'
    ],
}