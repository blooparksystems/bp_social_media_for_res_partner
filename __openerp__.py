# -*- coding: utf-8 -*-
##############################################################################
#
# Odoo, an open source suite of business apps
# This module copyright (C) 2015 bloopark systems (<http://bloopark.de>).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
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
