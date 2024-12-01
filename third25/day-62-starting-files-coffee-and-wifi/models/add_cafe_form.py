from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField
from wtforms.validators import DataRequired, URL

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = URLField('Cafe Location on Google Maps (URL)', validators=[URL(require_tld=True, message='Invalid URL')])
    open_time = StringField('Open time e.g 8AM', validators=[DataRequired()])
    close_time = StringField('Close time e.g 5:30PM', validators=[DataRequired()])
    
    # Reseña de café con opciones secuenciales
    coffee_rating = SelectField('Coffee Rating', choices=[
        ('☕️', '☕️'),          # Primera opción
        ('☕️☕️', '☕️☕️'),     # Segunda opción
        ('☕️☕️☕️', '☕️☕️☕️'), # Tercera opción
        ('☕️☕️☕️☕️', '☕️☕️☕️☕️'), # Cuarta opción
        ('☕️☕️☕️☕️☕️', '☕️☕️☕️☕️☕️') # Quinta opción
    ], validators=[DataRequired()])
    
    # Fuerza de wifi con opciones secuenciales
    wifi_strength = SelectField('Wifi Strength Raiting', choices=[
        ('💪', '💪'),
        ('💪💪', '💪💪'),
        ('💪💪💪', '💪💪💪'),
        ('💪💪💪💪', '💪💪💪💪'),
        ('💪💪💪💪💪', '💪💪💪💪💪')
    ], validators=[DataRequired()])
    
    # Enchufes disponibles con opciones secuenciales
    power_socket = SelectField('Power Socket Availibility', choices=[
        ('🔌', '🔌'),
        ('🔌🔌', '🔌🔌'),
        ('🔌🔌🔌', '🔌🔌🔌'),
        ('🔌🔌🔌🔌', '🔌🔌🔌🔌'),
        ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌')
    ], validators=[DataRequired()])
    
    submit = SubmitField('Submit')