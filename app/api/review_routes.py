from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, Review
from app.forms.review_form import ReviewForm, UpdateReviewForm

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


@review_routes.route('')
@login_required
def reviews():
    """
    Gets all reviews
    """
    reviews = Review.query.all()
    return {review.id: review.to_dict() for review in reviews}

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


@review_routes.route('/<int:id>', methods=["PUT"])
@login_required
def update_review(id):
    """
    Updates a review
    """
    form = UpdateReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        # if current_user.id == int(form.data['author_id']):
        review = Review.query.get(id)
        if review:
            review.content=form.data['content'],
            review.updated_at=form.data['updated_at']
            db.session.commit()
            return review.to_dict()
        else:
            return {'errors': ['Review not found.']}, 404
    return{'errors': validation_errors_to_error_messages(form.errors)}, 401

@review_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_review(id):
    """
    Deletes a review
    """
    review = Review.query.get(id)
    if review:
        db.session.delete(review)
        db.session.commit()
        return {"message": f'Review {id} successfully deleted'}
    else:
        return {'errors': ['Review not found.']}, 404
