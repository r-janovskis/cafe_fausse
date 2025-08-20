import os

from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

load_dotenv()

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)
    app.config['FLASK_APP'] = os.getenv('FLASK_APP')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

    # Enables CORS for all routes
    # This allows cross-origin requests, or in simple terms, allows the front-end (our React app) to communicate with the back-end
    CORS(app)


    db.init_app(app)


    # Import models (or tables)
    from .models import Customer, Reservation, Category, Menu

    # Associate models with the app context
    with app.app_context():
        db.create_all()

    # Create basic route to see if the app works
    # @app.route('/')
    # def index():
    #     return "Welcome to the Cafe Fausse!"
    
    # Register the public Blueprint
    from .public import public_bp

    app.register_blueprint(public_bp, url_prefix='/api')

    # @app.route('/customers')
    # def get_customers():
    #     customer_list = Customer.query.all()
    #     return jsonify({'customers': [{'customer_id': c.customer_id, 'customer_name': c.customer_name, 'email': c.email} for c in customer_list] })
    return app