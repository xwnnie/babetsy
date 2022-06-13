from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, ValidationError


def phone_validation(form, field):
    # Checking if a phone number is valid
    phone = field.data
    if not phone.isnumeric():
        raise ValidationError('do not use letters or symbols like - or ( ).')
    if len(str(phone)) != 10:
        raise ValidationError('must be 10 digits.')

class AddressForm(FlaskForm):
    address = StringField(
        'address', validators=[DataRequired()])
    full_name = StringField(
        'full_name', validators=[DataRequired()])
    phone = StringField(
        'phone', validators=[DataRequired(), phone_validation])
