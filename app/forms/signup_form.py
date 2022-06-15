from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, ValidationError, Length
from app.models import User


def user_exists(form, field):
    # Checking if user exists
    email = field.data
    user = User.query.filter(User.email == email).first()
    if user:
        raise ValidationError('Email address is already in use.')


def username_exists(form, field):
    # Checking if username is already in use
    username = field.data
    user = User.query.filter(User.username == username).first()
    if user:
        raise ValidationError('Username is already in use.')


def phone_validation(form, field):
    # Checking if a phone number is valid
    phone = field.data
    if not phone.isnumeric():
        raise ValidationError('do not use letters or symbols like - or ( ).')
    if len(str(phone)) != 10:
        raise ValidationError('must be 10 digits.')



class SignUpForm(FlaskForm):
    username = StringField(
        'Username', validators=[DataRequired(), username_exists, Length(min=1, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email(), user_exists, Length(min=1, max=30)])
    password = StringField('Password', validators=[DataRequired(), Length(min=1, max=20)])
    address = StringField('Address', validators=[DataRequired(), Length(min=1, max=100)])
    phone = StringField('Phone', validators=[DataRequired(), phone_validation, Length(min=1, max=20)])
    full_name = StringField('Full Name', validators=[
                            DataRequired(), Length(min=1, max=30)])
