from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.models import db, User
from app.forms.address_form import AddressForm

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
    return user.to_dict()


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