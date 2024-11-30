from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectMultipleField, SelectField
from wtforms.validators import DataRequired, URL
import csv


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = URLField('Cafe Location on Google Maps (URL)', validators=[URL(require_tld=True, message='Invalid URL')])
    open_time = StringField('Open time e.g 8AM', validators=[DataRequired()])
    close_time = StringField('Close time e.g 5:30PM', validators=[DataRequired()])
    
    # Reseña de café con opciones secuenciales
    coffe_raiting = SelectField('Coffee Raiting', choices=[
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
    
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe = form.cafe.data
        location = form.location.data
        open_time = form.open_time.data
        close_time = form.close_time.data
        coffe_raiting = form.coffe_raiting.data
        wifi_strength = form.wifi_strength.data
        power_socket = form.power_socket.data
        with open('cafe-data.csv', mode='a', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file, lineterminator='\r\n')
            csv_writer.writerow([cafe, location, open_time, close_time, coffe_raiting, wifi_strength, power_socket])
        return redirect('cafes')
        
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', header=list_of_rows[0], cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
