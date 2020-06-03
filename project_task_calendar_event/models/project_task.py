# -*- coding: utf-8 -*-
# Copyright 2020 Therp BV - https://therp.nl.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class ProjectTask(models.Model):
    """Extend task with planning information."""
    _inherit = "project.task"

    calendar_event_ids = fields.One2many(
        comodel_name="calendar.event",
        string="Planning"
    )
