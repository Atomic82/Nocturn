from flask_wtf import FlaskForm
from wtforms import StringField, submitField, TextAreaField
from wtforms.validators import DataRequired

class BlogPostFrom(FlaskForm):
    title = StringField('Title', validators=[DataRequired])
    text = TextAreaField('Text', validators=[DataRequired])
    submit = SubmitField('Post')