from datetime import timedelta

from odoo import api, fields, models


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Real Estate Property Offer"

    # Basic fields
    price = fields.Float()
    status = fields.Selection(
        selection=[
            ("accepted", "Accepted"),
            ("refused", "Refused"),
        ],
        copy=False,
    )
    validity = fields.Integer(
        help="Offer validity in days",
        default=7,
    )

    # Relational fields
    partner_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)

    # Computed fields
    date_deadline = fields.Date(
        compute="_compute_date_deadline", inverse="_inverse_date_deadline"
    )

    @api.depends("create_date", "validity")
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                create_date = fields.Datetime.from_string(record.create_date)
                record.date_deadline = create_date + timedelta(days=record.validity)
            else:
                record.date_deadline = fields.Date.today() + timedelta(
                    days=record.validity
                )

    def _inverse_date_deadline(self):
        print("inverse_date_deadline\n\n")
        for record in self:
            if record.date_deadline:
                record.validity = (record.date_deadline - fields.Date.today()).days
            else:
                record.validity = 7
