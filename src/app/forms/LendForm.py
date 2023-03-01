from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField


class LendForm(FlaskForm):
    amount = IntegerField('amount')



