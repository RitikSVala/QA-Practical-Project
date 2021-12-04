from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired

class InputForm(FlaskForm):
    name = StringField('name', validators=[InputRequired()])
    birth_date = StringField('name', validators=[InputRequired()])

    