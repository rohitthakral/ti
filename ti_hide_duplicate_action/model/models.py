# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, api, fields,_
from logging import getLogger
from lxml import etree

_logger = getLogger(__name__)

class BaseModel(models.AbstractModel):
    _inherit = 'base'


    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):

        res = super(BaseModel,self).fields_view_get(view_id=view_id,view_type=view_type, toolbar=toolbar, submenu=submenu)
        if view_type == 'form' and not self.env.user.user_has_groups('base.group_system'):
            doc = etree.XML(res['arch'])
            for node in doc.xpath("//form"):
                node.set("duplicate", "0")

            res['arch'] = etree.tostring(doc, encoding='unicode')
        return res