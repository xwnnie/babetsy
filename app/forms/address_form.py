from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class AddressForm(FlaskForm):
    address = StringField(
        'address', validators=[DataRequired()])
    full_name = StringField(
        'full_name', validators=[DataRequired()])
    phone = StringField(
        'phone', validators=[DataRequired()])
