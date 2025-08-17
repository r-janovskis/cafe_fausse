from flask import Blueprint

# create the Blueprint for the API calls
public_bp = Blueprint('api', __name__)

# Import routes to register them with the Blueprints
from . import menu, reservation, newsletter
