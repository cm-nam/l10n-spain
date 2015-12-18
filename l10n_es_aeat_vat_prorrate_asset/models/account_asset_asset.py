# -*- coding: utf-8 -*-
# © 2015 Antiun Ingeniería S.L.
# © 2015 Pedro M. Baeza <pedro.baeza@serviciosbaeza.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import fields, models


class AccountAssetAsset(models.Model):
    _inherit = 'account.asset.asset'

    vat_prorrate_percent = fields.Float()
    vat_prorrate_increment = fields.Float()
