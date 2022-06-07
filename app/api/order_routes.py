from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, Order
from app.forms.order_form import OrderForm

order_routes = Blueprint('orders', __name__)


def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{field} : {error}')
    return errorMessages


@order_routes.route('', methods=["POST"])
@login_required
def create_order():
    """
    Creates an order
    """
    form = OrderForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        # if current_user.id == int(form.data['buyer_id']):
        order = Order(
            buyer_id = int(form.data['buyer_id']),
            product_id = int(form.data['product_id']),
            quantity=int(form.data['quantity']),
            order_number = form.data['order_number'],
            created_at = form.data['created_at']
        )
        db.session.add(order)
        db.session.commit()
        return order.to_dict()
    return{'errors': validation_errors_to_error_messages(form.errors)}, 401

@order_routes.route('/<order_number>', methods=['DELETE'])
@login_required
def delete_order(order_number):
    """
    Delete all orders associated to a order_number 
    """
    orders = Order.query.filter(Order.order_number == order_number).all()
    if orders:
        for order in orders:
            db.session.delete(order)
        db.session.commit()
        return {"message": f'all orders associated to {order_number} successfully deleted'}
    else:
        return {'errors': ['Orders not found.']}, 404
