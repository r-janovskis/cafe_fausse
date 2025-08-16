from . import public_bp
from flask import jsonify, request

@public_bp.route('/reservation', methods = ['POST'])
def reserve_table():
    # Imoport models for Reservation and Customer tables
    from ..models import Reservation, Customer

    return ""