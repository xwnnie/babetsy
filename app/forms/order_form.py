from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, DateTimeField, FieldList, FormField
from wtforms.validators import DataRequired


class ProductForm(FlaskForm):
    product_id = IntegerField('product_id', validators=[DataRequired()])
    quantity = IntegerField('quantity', validators=[DataRequired()])

class OrderForm(FlaskForm):
    buyer_id = IntegerField('buyer_id', validators=[DataRequired()])
    products = FieldList(FormField(ProductForm))
    order_number = StringField('order_number', validators=[DataRequired()])
    created_at = StringField('created_at')
