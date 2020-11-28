
from odoo import models, fields, api


class Openacademycourses(models.Model):
    _name = "openacademy.courses"
    _description = "Openacademy Courses"

    name = fields.Char(string="name", required=True)

    description = fields.Text(string="Description")
    responsible_id = fields.Many2one(
        'openacademy.partner', string="Responsible", ondelete='cascade')
    session_ids = fields.One2many(
        'openacademy.sessions', 'course_id', string="Sessions")
    level = fields.Selection[('Easy', 'Easy'),
     ('Medium', 'Medium'),
     ('Hard', 'Hard'),
      ]


class Openacademysessions(models.Model):
    _name = "openacademy.sessions"
    _description = "Openacademy Sessions"

    name = fields.Char(string="name", required=True)
    state = fields.Selection(
        [('draft', 'Draft'),
         ('confirmed', 'Confirmed'),
            ('done', 'Done')],
        default='Draft')
    start_date = fields.Date(string="Start Date", default="Date today")
    end_date = fields.Date(string="End Date", default="Date today")
    duration = fields.Float(string="Duration", default="One day")
    instructor_id = fields.Many2one(
        'openacademy.partner', string="instructor_id", ondelete='cascade')
    course_id = fields.Many2one(
        'openacademy.courses', ondelete='cascade', required=True)
    attendee_ids = fields.Many2many('openacademy.partner', string="Attendee")
    Active = fields.Boolean("Active", default=True)
    seats = fields.Integer(string="Number of seats")
    taken_seats = fields.Float(string="Taken seats", computed="_taken_seats")
@api.depends('seats', 'attendee_ids')
def _taken_seats(self):
    for record in self:
        record.taken_seats = 100*len(record.attendee_ids)/record.seats
        if record.taken_seats > 100:
            return ('Error', record.seats-record.taken_seats*100, len(record.attendee_ids))


class Openacademypartner(models.Model):
    _name = "openacademy.partner"
    _description = "Openacademy Partner"

    name = fields.Char(string="Name")
    instructor = fields.Boolean(string="Instructor")
    session_ids = fields.Many2many('openacademy.sessions', readonly=True)
