# -*- coding: utf-8 -*-
# © 2015 Antiun Ingeniería S.L.
# © 2015 Pedro M. Baeza <pedro.baeza@serviciosbaeza.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import api, fields, models


class L10nEsAeatMod303Report(models.Model):
    _inherit = 'l10n.es.aeat.mod303.report'

    asset_prorrate_regularization_account = fields.Many2one(
        comodel_name="account.account",
        string="Asset regularization account",
        help="This account will be the account where charging the "
             "regularization of the assets that has increased its value "
             "due to the vat prorrate.")

    @api.multi
    def _prepare_regularization_extra_move_lines(self):
        lines = super(L10nEsAeatMod303Report,
                      self)._prepare_regularization_extra_move_lines()
        if (self.vat_prorrate_type != 'general' or
                self.period_type not in ('4T', '12')):
            return lines
        year = fields.from_string(self.fiscalyear_id.date_start).year
        assets = self.env['account.asset'].search(
            [('purchase_date', 'like', '%s%%' % year)])
        for asset in assets:
            if not asset.vat_prorrate_increment:
                continue

        return lines
