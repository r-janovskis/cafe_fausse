from . import public_bp
from flask import jsonify, request
from sqlalchemy import and_
from datetime import datetime, timedelta
import random

from .. import db

@public_bp.route('/reservation', methods = ['POST'])
def reserve_table():
    # Imoport models for Reservation and Customer tables
    from ..models import Reservation, Customer

    # Get the data from request
    table_reservation = request.get_json()

    # Check if the customer exists
    customer = Customer.query.filter_by(email = table_reservation['email']).first()
    # We have a new customer
    # let's add it to the database
    if not customer:
        new_customer = Customer(
            customer_name = table_reservation['name'],
            email = table_reservation['email'],
            phone_number = table_reservation['phone_number']
        )
        db.session.add(new_customer)
        db.session.commit()
        customer = new_customer

    # Check table availability
    # our reservations are for 2 hours
    # so we check the availablity of tables from 2h before the requested time and 2h after
    # date in format: YYYY=MM-DD
    # time in format: HH:MM:00
    
    reservation_time = table_reservation['date'] + " " + table_reservation['time']
    reservation_object = datetime.strptime(reservation_time, '%Y-%m-%d %H:%M:%S')

    booked_reservations = Reservation.query.filter(and_(
        Reservation.timeslot > reservation_object - timedelta(hours = 2),
        Reservation.timeslot < reservation_object + timedelta(hours = 2)
    ))

    # Our tables are numbered from 1 to 30
    free_tables = [i for i in range(1, 31)]

    # Check out tables that are taken
    for reservation in booked_reservations:
        if reservation.table_nr in free_tables:
            free_tables.remove(reservation.table_nr)

    if len(free_tables) == 0:
        return jsonify({'message': "We are sorry, but there are no free tables left for this time."}), 400

    # We select a random table from the free tables
    table_for_booking = random.choice(free_tables)

    # Create a new reservattion and save it to the database
    new_reservation = Reservation(
        timeslot = reservation_time,
        customer_id = customer.customer_id,
        number_of_people = table_reservation['number_of_guests'],
        table_nr = table_for_booking
    )

    db.session.add(new_reservation)
    db.session.commit()



    
    return jsonify({'message': "Your booking has been successful!"}), 201