# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import SUPERUSER_ID, _, api

_logger = logging.getLogger(__name__)


def post_init_hook(cr, e):
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})

        new_value = "Québec"
        crm_team_ids = env["crm.team"].search([])
        if crm_team_ids:
            for crm_team_id in crm_team_ids:
                if crm_team_id.name == "Sales":
                    crm_team_id.write({"name": new_value})
        crm_team_translation_ids = env["ir.translation"].search(
            [
                ("module", "=", "sales_team"),
                ("type", "=", "model"),
                ("name", "=", "crm.team,name"),
                ("src", "=", "Europe"),
            ]
        )
        if crm_team_translation_ids:
            for crm_team_translation_id in crm_team_translation_ids:
                crm_team_translation_id.write(
                    {"src": new_value, "value": new_value}
                )
