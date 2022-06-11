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
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        payload = request.get_json()
        if payload and payload["products"]:
            for product in payload["products"]:
                order = Order(
                    buyer_id=int(payload['buyer_id']),
                    product_id=int(product['id']),
                    quantity=int(product['quantity']),
                    order_number=payload['order_number'],
                    created_at=payload['created_at'],
                    full_name=payload['full_name'],
                    phone=payload['phone'],
                    address=payload['address']
                )
                # if order:
                #     print("new order")
                db.session.add(order)
            db.session.commit()
            order_number = payload['order_number']
            all_orders = Order.query.filter(
                Order.order_number == order_number).all()
            if all_orders:
                return {order_number: [order.to_dict() for order in all_orders]}
            else:
                return {'message': 'no orders created'}
        else:
            return{'errors': "wrong format of payload"}, 401
    return{'errors': "wrong header"}, 401
    
    # form = OrderForm()
    # form['csrf_token'].data = request.cookies['csrf_token']
    # # print("before submitted********", form.products.data)
    # if form.validate_on_submit():
    #     # if current_user.id == int(form.data['buyer_id']):
    #     print("submitted********", form.products)
    #     for field in form.products:
    #         print("+++++++++", field.product_id.data)
    #         order = Order(
    #             buyer_id = int(form.data['buyer_id']),
    #             product_id = int(field.product_id.data),
    #             quantity=int(field.quantity.data),
    #             order_number = form.data['order_number'],
    #             created_at = form.data['created_at']
    #         )
    #         if order:
    #             print("new order")
    #         db.session.add(order)

    #     db.session.commit()
    #     order_number = form.data['order_number']
    #     all_orders = Order.query.filter(
    #         Order.order_number == order_number).all()
    #     if all_orders:
    #         return {order_number: [order.to_dict() for order in all_orders]}
    #     else:
    #         return {'message': 'no orders created'}
    # return{'errors': validation_errors_to_error_messages(form.errors)}, 401


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
        return {"message": f'all purchases associated to {order_number} successfully deleted'}
    else:
        return {'errors': ['Order {order_number} not found.']}, 404
