from flask_wtf import FlaskForm 
from wtforms import StringField
from wtforms.fields.core import BooleanField
from wtforms.validators import DataRequired

    
class Plytoteka(FlaskForm):
    wykonawca = StringField('wykonawca', validators=[DataRequired()])
    album = StringField('album', validators=[DataRequired()])
    czy_posiadam = BooleanField('posiadam')