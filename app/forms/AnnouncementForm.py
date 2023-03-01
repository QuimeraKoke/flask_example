from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField


class AnnouncementForm(FlaskForm):
    title = StringField('title')
    description = TextAreaField('description')
    amount = IntegerField('amount')


