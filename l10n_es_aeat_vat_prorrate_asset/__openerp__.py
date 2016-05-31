# -*- coding: utf-8 -*-
# © 2015 Antiun Ingeniería S.L.
# © 2015 Pedro M. Baeza <pedro.baeza@serviciosbaeza.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "AEAT - Prorrata de IVA - Extensión para los activos",
    "version": "8.0.1.0.0",
    "license": "AGPL-3",
    "author": "Antiun Ingeniería S.L., "
              "Serv. Tecnol. Avanzados - Pedro M. Baeza, "
              "Odoo Community Association (OCA)",
    "website": "http://www.antiun.com",
    "category": "Accounting",
    "depends": [
        'l10n_es_aeat_vat_prorrate',
        'account_asset',
    ],
    "data": [
        'views/account_asset_asset_view.xml',
        'views/account_invoice_view.xml',
        'views/mod303_view.xml',
    ],
    "installable": True,
}
