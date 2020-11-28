from odoo import fields, models, api


class Librarybook(models.Model):
    _name = "Library.book"
    _discription = "Library Book"

    name = fields.Char(string="Name")
    author_ids = fields.Many2many('library.partner', string="Autor",
        domain=[('journal_id_type', '=', 'bank'), ('payment_type', '=', 'inbound')],
        widget="many2many_tags")


    edition_date = fields.Date(string="Edition date")
    isbn = fields.Char(string="Isbn")
    publisher_id = fields.Many2one(
        'library.publisher', string="Publisher", ondelete='cascade')
    rental_ids = fields.One2many('library.rental', 'book_id', string="Rental")


class Libraryrental(models.Model):
    _name = "Library.rental"
    _description = "Library Rental"

    customer_id = fields.Many2one(
        'library.partner', 'customer_email', string='Customer', ondelete='cascade')
    book_id = fields.Many2one(
        'library.book', string="Book", ondelete='cascade')
    rental_date = fields.Date(string="Rental date")
    return_date = fields.Date(string="Return date")
    customer_address = fields.Char(
        related='customer_id.address', store=True, string='Customer address')
    customer_email = fields.Char(
        related='customer_id.email', store=True, string='Customer email')
    book_authors = fields.Char(
        related='book_id.author_ids', store=True, string='Book authors')
    book_edition_date = fields.Date(related='book_id.edition_date', store=True, string='Book - edition date')
    book_publisher = fields.Char(related='book_id.name', store=True, string='Book publisher')



class Librarypartner(models.Model):
    _name = "Library.partner"
    _discriotion = "Library Partner"

    name = fields.Char(string="Name")
    email = fields.Char(string="e-mail")
    address = fields.Text(string="address")
    partner_type = fields.Selection[
        ('customer', 'Customer'),
        ('author', 'Author')
    ]
    rental_ids = fields.One2many('library.rental',
                                 'rental_ids', ondelete='cascade', string="Rental")


class Librarypublisher(models, Model):
    _name = "Library.publisher"
    _discription = "Library Publisher"

    name = fields.Char(string="Name")


