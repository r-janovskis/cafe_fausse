from . import db
from sqlalchemy import TIMESTAMP

class Customer(db.Model):
    __tablename__ = 'customers'
    customer_id = db.Column(db.Integer, primary_key = True)
    customer_name = db.Column(db.String(50))
    email = db.Column(db.String(75), unique = True, nullable = False)
    phone_number = db.Column(db.String(15))
    newsletter_signup = db.Column(db.Boolean, nullable = False, default = False)

    def __repr__(self):
        return f"Customer with email '{self.email}' registered."
    

class Reservation(db.Model):
    __tablename__ = 'reservations'
    reservation_id = db.Column(db.Integer, primary_key = True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.customer_id', ondelete="SET NULL", onupdate="CASCADE"))
    number_of_people = db.Column(db.Integer, nullable = False)
    timeslot = db.Column(TIMESTAMP, nullable = False)
    table_nr = db.Column(db.Integer, db.CheckConstraint('table_nr > 0 AND table_nr <= 30', name = "table_nr_check"), nullable = False)

    def __repr__(self):
        return f"Customer with ID '{self.customer_id}' made a reservation for {self.number_of_people} people at table {self.table_nr} for {self.timeslot}."


class Category(db.Model):
    __tablename__ = 'categories'
    category_id = db.Column(db.Integer, primary_key = True)
    category_name = db.Column(db.String(30), unique = True, nullable = False)

    def __repr__(self):
        return f"Category '{self.category_name}' with ID {self.category_id} created."
    

class Menu(db.Model):
    __tablename__ = 'menu'
    item_id = db.Column(db.Integer, primary_key = True)
    item_name = db.Column(db.String(50), nullable = False, unique = True)
    item_price = db.Column(db.Numeric(5, 2), nullable = False)
    item_category = db.Column(db.Integer, db.ForeignKey('categories.category_id', ondelete = "SET NULL", onupdate = "CASCADE"))

    def __repr__(self):
        return f"{self.item_name} added to the menu."