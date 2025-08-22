from flask import jsonify, request
from sqlalchemy import and_
from datetime import datetime, timedelta
import random

from . import public_bp

from ..models import Reservation, Customer
from .. import db

@public_bp.route('/reservation', methods = ['POST'])
def reserve_table():
    # Imoport models for Reservation and Customer tables
    

    # Get the data from request
    table_reservation = request.get_json()

    # Check if the customer exists
    customer = Customer.query.filter_by(email = table_reservation['email']).first()
    
    if customer:
        # Let's check if we have the name and phone number for the customer
        if not customer.customer_name:
            setattr(customer, 'customer_name', table_reservation['name'])
            db.session.commit()
        if not customer.phone_number and table_reservation.get('phone_number'):
            setattr(customer, 'phone_number', table_reservation.get('phone_number') or None)
            db.session.commit()
    else:
        # We have a new customer
        # let's add it to the database
        new_customer = Customer(
            customer_name = table_reservation['name'],
            email = table_reservation['email'],
            # We handle it this differently as phone_number is optional 
            # and in case it's not provided or is empty we set it to None (or null for the database)
            phone_number = table_reservation.get('phone_number') or None
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

    # Check if the reservation is in the future
    if reservation_object <= datetime.now():
        return jsonify({'message': "Ohh, no... Looks like you are trying to make a reservation in the past!"}), 400



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

    # Case where we don't have free tables for the selected time
    if len(free_tables) == 0:
        return jsonify({'message': "We are sorry, but there are no free tables left for this time."}), 400
    
    # Check for double booking
    for reservation in booked_reservations:
        if reservation.customer_id == customer.customer_id:
            return jsonify( {'message': "You already have a booking overlapping with the selected time!"} ), 400

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