# -*- coding: utf-8 -*-
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
