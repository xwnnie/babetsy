from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.models import db, User, Product, Order
from app.forms.address_form import AddressForm
from sqlalchemy import distinct

user_routes = Blueprint('users', __name__)


def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{field} : {error}')
    return errorMessages

@user_routes.route('/')
@login_required
def users():
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}


@user_routes.route('/<int:id>')
@login_required
def user(id):
    """
    Gets a user's info, order history, favorites
    """
    user = User.query.get(id)
    user_dict = user.to_dict()
    orders = Order.query.filter(Order.buyer_id == id).distinct(Order.order_number).all()
    order_numbers = [order.order_number for order in orders]
    for order_number in order_numbers:
        all_orders = Order.query.filter(Order.order_number == order_number).all()
        user_dict["orders"][order_number] = [order.to_dict() for order in all_orders]
    return user_dict


@user_routes.route('/<int:id>', methods=["PUT"])
@login_required
def update_address(id):
    """
    Updates a user's shipping address
    """
    form = AddressForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        user = User.query.get(id)
        if user:
            user.address = form.data['address']
            db.session.commit()
            return user.to_dict()
        else:
            return {'errors': ['User does not exist']}, 404
    return{'errors': validation_errors_to_error_messages(form.errors)}, 401


@user_routes.route('/<int:user_id>/favorites/<int:product_id>', methods=["POST"])
@login_required
def add_favorite(user_id, product_id):
    user = User.query.get(user_id)
    product = Product.query.get(product_id)
    if user and product:
        user.favorite_products.append(product)
        db.session.commit()
        return {"message": "favorite successfully added"}
    else:
        return {'errors': ['User or Product does not exist']}, 404


@user_routes.route('/<int:user_id>/favorites/<int:product_id>', methods=["DELETE"])
@login_required
def delete_favorite(user_id, product_id):
    user = User.query.get(user_id)
    product = Product.query.get(product_id)
    if user and product:
        user.favorite_products.remove(product)
        db.session.commit()
        return {"message": "favorite successfully deleted"}
    else:
        return {'errors': ['User or Product does not exist']}, 404
