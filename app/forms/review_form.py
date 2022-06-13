from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, DateField, TextAreaField
from wtforms.validators import DataRequired, Length


class ReviewForm(FlaskForm):
    author_id = IntegerField('author_id', validators=[DataRequired()])
    product_id = IntegerField('product_id', validators=[DataRequired()])
    content = TextAreaField('content', validators=[DataRequired(), Length(min=1, max=500)])
    created_at = StringField('created_at') 
    updated_at = StringField('updated_at')


class UpdateReviewForm(FlaskForm):
    content = TextAreaField('content', validators=[DataRequired(), Length(min=1, max=500)])
    updated_at = StringField('updated_at')
