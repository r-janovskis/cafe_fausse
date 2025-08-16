from . import public_bp
from flask import jsonify

@public_bp.route('/menu', methods=['GET'])
def get_menu():
    # Import the Menu model
    from ..models import Menu, Category

    # Query all menu items and their categories
    menu_items = Menu.query.all()

    # Prepare a list of items to be retuned
    menu_list = []
    for item in menu_items:
        menu_list.append({
            'name': item.item_name,
            'description': item.item_description,
            'price': '$ {:.2f}'.format(item.item_price),
            'category': Category.query.filter_by(category_id=item.item_category).first().category_name
        })


    return jsonify({'menu': menu_list}), 200