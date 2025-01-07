# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Real Estate",
    "depends": [
        # 'base_setup',
        "base",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/estate_property_views.xml",
        "views/estate_menus.xml",
    ],
    # "demo": [],
    # "css": [],
    "installable": True,
    "application": True,
    "auto_install": True,
}
