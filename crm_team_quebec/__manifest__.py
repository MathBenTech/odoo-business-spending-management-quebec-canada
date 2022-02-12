# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "crm_team_quebec",
    "version": "12.0.0.1",
    "author": "MathBenTech",
    "website": "https://mathben.tech",
    "license": "AGPL-3",
    "category": "Extra tools",
    "summary": "Set by default Quebec to sale team in CRM",
    "description": """
crm_team_quebec
===============
Change the name of sales team in CRM, replace french Europe to Québec.
""",
    "depends": [
        "crm",
        "sales_team",
    ],
    "post_init_hook": "post_init_hook",
    "installable": True,
}
