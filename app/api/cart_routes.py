from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, Cart
from app.forms.cart_form import CartForm

cart_routes = Blueprint('cart', __name__)


def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{field} : {error}')
    return errorMessages


@cart_routes.route('', methods=["POST"])
@login_required
def create_cart():
    """
    Adds a new product item to cart table
    """
    form = CartForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        # if current_user.id == int(form.data['author_id']):
        cart = Cart(
            buyer_id=int(form.data['buyer_id']),
            product_id=int(form.data['product_id']),
            quantity=form.data['quantity']
        )
        db.session.add(cart)
        db.session.commit()
        return cart.to_dict()
    return{'errors': validation_errors_to_error_messages(form.errors)}, 401


@cart_routes.route('/<int:buyer_id>/<int:product_id>', methods=['PUT'])
@login_required
def update_cart(buyer_id, product_id):
    """
    Updates quantity of an item in cart 
    """
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        payload = request.get_json()
        cart = Cart.query.filter(
            Cart.buyer_id == buyer_id, Cart.product_id == product_id).one()
        if cart:
            cart.quantity = payload["quantity"]
            db.session.commit()
            return cart.to_dict()
        else:
            return {'errors': ['cart item {product_id} not found.']}, 404
    return {'errors': "not valid content type"}, 401


@cart_routes.route('/<int:buyer_id>/<int:product_id>', methods=['DELETE'])
@login_required
def delete_cart_item(buyer_id, product_id):
    """
    Delete an item from cart
    """
    cart = Cart.query.filter(Cart.buyer_id==buyer_id, Cart.product_id==product_id).one()
    if cart:
        db.session.delete(cart)
        db.session.commit()
        return {"message": f'cart item {product_id} successfully deleted'}
    else:
        return {'errors': ['cart item {product_id} not found.']}, 404


@cart_routes.route('/<int:buyer_id>/clear', methods=['DELETE'])
@login_required
def clear_cart(buyer_id):
    """
    Clears all cart items of a buyer
    """
    carts = Cart.query.filter(Cart.buyer_id == buyer_id).all()
    if carts:
        for cart in carts:
            db.session.delete(cart)
        db.session.commit()
        return {"message": f'cart items of buyer {buyer_id} successfully deleted'}
    else:
        return {'errors': ['no cart item of buyer {buyer_id} found.']}, 404
