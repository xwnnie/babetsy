from tokenize import String
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, DateTimeField
from wtforms.validators import DataRequired


class OrderForm(FlaskForm):
    buyer_id = IntegerField('buyer_id', validators=[DataRequired()])
    product_id = IntegerField('product_id', validators=[DataRequired()])
    quantity = IntegerField('quantity', validators=[DataRequired()])
    order_number = StringField('order_number', validators=[DataRequired()])
    created_at = StringField('created_at')
