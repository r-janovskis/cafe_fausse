from flask import request, jsonify

from . import public_bp

from .. import db
from ..models import Customer

@public_bp.route('/newsletter', methods = ['POST'])
def subscribe_newsletter():
    # Retrieve the data from the request
    subscribtion_data = request.get_json()

    # Check if we already have this customer in the database
    customer = Customer.query.filter_by(email=subscribtion_data['email']).first()

    if customer:
        # Customer is already in the database
        # We just update the newsletter_signup value for this customer
        setattr(customer, 'newsletter_signup', True)
    else:
        # Create a new customer entry
        # and add it to the database
        customer = Customer(
            email=subscribtion_data['email'],
            newsletter_signup = True
        )
        db.session.add(customer)

    # Commit the changes to the database
    db.session.commit()

    return jsonify({'message': 'Thank you for subscribing to our newsletter!'}), 201