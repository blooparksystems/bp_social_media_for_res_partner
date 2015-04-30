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
from openerp.models import Model
from openerp import fields


class Partner(Model):
    _inherit = "res.partner"

    linkedin = fields.Char(
        'Linkedin', help="Social Media Link of Partner or Company")
    behance = fields.Char(
        'Behance', help="Social Media Link of Partner or Company")
    dribbble = fields.Char(
        'Dribbble', help="Social Media Link of Partner or Company")
    github = fields.Char(
        'Github', help="Social Media Link of Partner or Company")
    google_plus = fields.Char(
        'Google Plus', help="Website of Partner or Company")
    facebook = fields.Char(
        'Facebook', help="Social Media Link of Partner or Company")
    twitter = fields.Char(
        'Twitter', help="Social Media Link of Partner or Company")
