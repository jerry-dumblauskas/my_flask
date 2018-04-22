from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField
from wtforms.validators import DataRequired


class CalcForm(FlaskForm):
    cylinders = IntegerField('Cylinders', validators=[DataRequired()])
    horsepower = IntegerField('Horsepower', validators=[DataRequired()])
    submit = SubmitField('Calculate')
