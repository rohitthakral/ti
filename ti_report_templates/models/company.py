# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ResCompany(models.Model):
    _inherit = "res.company"

    stamp_image = fields.Binary("Company Stamp")
