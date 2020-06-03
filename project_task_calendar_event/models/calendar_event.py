# -*- coding: utf-8 -*-
# Copyright 2020 Therp BV - https://therp.nl.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class CalendarEvent(models.Model):
    _inherit = "calendar.event"

    task_id = fields.Many2one(
        comodel_name="project.task",
        string="Task"
    )
