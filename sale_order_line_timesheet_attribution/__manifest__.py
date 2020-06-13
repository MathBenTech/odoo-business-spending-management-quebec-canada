# Copyright 2020 TechnoLibre <info@technolibre.ca>
# License AGPLv3.0 or later (https://www.gnu.org/licenses/agpl-3.0.en.html).
{
    "name": "Sale order line timesheet attribution",
    "summary": "Associate manually timesheet to sale order line",
    "category": "Project",
    "version": "12.0.0.0.0",
    "license": "AGPL-3",
    "author": "TechnoLibre",
    "depends": [
        "hr_timesheet",
        "project",
        "sale_timesheet",
        "sale",
    ],
    "data": [
        "views/project_task_views.xml",
    ],
    "demo": [],
    "application": False,
    "installable": True,
}
