from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, Review
from app.forms.review_form import ReviewForm

review_routes = Blueprint('reviews', __name__)


def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{field} : {error}')
    return errorMessages


@review_routes.route('', methods=["POST"])
@login_required
def create_review():
    """
    Creates a review
    """
    form = ReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        # if current_user.id == int(form.data['author_id']):
        print("submitted")
        review = Review(
            author_id=int(form.data['author_id']),
            product_id=int(form.data['product_id']),
            content=form.data['content'],
            created_at=form.data['created_at'],
            updated_at=form.data['updated_at']
        )
        db.session.add(review)
        db.session.commit()
        return review.to_dict()
    return{'errors': validation_errors_to_error_messages(form.errors)}, 401


@review_routes.route('', methods=["POST"])
@login_required
def create_review():
    """
    Creates a review
    """
    form = ReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        # if current_user.id == int(form.data['author_id']):
        print("submitted")
        review = Review(
            author_id=int(form.data['author_id']),
            product_id=int(form.data['product_id']),
            content=form.data['content'],
            created_at=form.data['created_at'],
            updated_at=form.data['updated_at']
        )
        db.session.add(review)
        db.session.commit()
        return review.to_dict()
    return{'errors': validation_errors_to_error_messages(form.errors)}, 401

# @order_routes.route('/<order_number>', methods=['DELETE'])
# @login_required
# def product(order_number):
#     """
#     Delete all orders associated to a order_number 
#     """
#     orders = Order.query.filter(Order.order_number == order_number).all()
#     if orders:
#         for order in orders:
#             db.session.delete(order)
#         db.session.commit()
#         return {"message": f'all orders associated to {order_number} successfully deleted'}
#     else:
#         return {'errors': ['Orders not found.']}, 404
