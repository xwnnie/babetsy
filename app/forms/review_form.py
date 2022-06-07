from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, DateField, TextAreaField
from wtforms.validators import DataRequired


class ReviewForm(FlaskForm):
    author_id = IntegerField('author_id', validators=[DataRequired()])
    product_id = IntegerField('product_id', validators=[DataRequired()])
    content = TextAreaField('content', validators=[DataRequired()])
    created_at = StringField('created_at') 
    updated_at = StringField('updated_at')
