from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, ValidationError
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
        'username', validators=[DataRequired(), username_exists])
    email = StringField('email', validators=[DataRequired(), Email(), user_exists])
    password = StringField('password', validators=[DataRequired()])
    address = StringField('address', validators=[DataRequired()])
    phone = StringField('phone', validators=[DataRequired(), phone_validation])
    full_name = StringField('full_name', validators=[DataRequired()])
    
