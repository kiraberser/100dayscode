from flask import Flask, render_template, redirect
import csv

from models.add_cafe_form import CafeForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
    
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
        coffee_rating = form.coffee_rating.data
        wifi_strength = form.wifi_strength.data
        power_socket = form.power_socket.data
        with open('cafe-data.csv', mode='a', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file, lineterminator='\r\n')
            csv_writer.writerow([cafe, location, open_time, close_time, coffee_rating, wifi_strength, power_socket])
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
