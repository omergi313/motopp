from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField, IntegerField
from wtforms.validators import DataRequired


class AddBikeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    make = TextAreaField('Make', validators=[DataRequired()])
    model = TextAreaField('Model', validators=[DataRequired()])
    year = IntegerField('Year', validators=[DataRequired()])
    submit = SubmitField('Submit')
