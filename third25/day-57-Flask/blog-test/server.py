import requests
from flask import Flask, render_template
import random
from datetime import datetime
from urllib.parse import quote
import logging

app = Flask(__name__)

gender_enpoint = 'https://api.genderize.io?name='
agify_endpoint = 'https://api.agify.io?name='

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.now().year
    return render_template('index.html', num=random_number, year=current_year)

@app.route('/guess/<name>')
def guess_page(name):
    try:
        guess_name = quote(name).capitalize()
        guess_gender_response = requests.get(url=f'{gender_enpoint}{guess_name}')
        guess_age_response = requests.get(url=f'{agify_endpoint}{guess_name}')

        if guess_age_response.status_code == 200 and guess_gender_response.status_code == 200:
            guess_gender = guess_gender_response.json()
            guess_age = guess_age_response.json()
        else: 
            guess_gender = 'lo sentimos no encontramos tú nombre'
            guess_age = 'lo sentimos no encontramos tú edad'
    except requests.exceptions.RequestException as e:
        logging.error(f'Error al hacer una solicitud {e}')
    return render_template('guess.html', gender=guess_gender, age=guess_age, name=guess_name)

@app.route('/blog/<int:num>')
def blog_page(num):
    blogs_response = requests.get(url='https://api.npoint.io/c790b4d5cab58020d391')
    blogs_data = blogs_response.json() 
    not_founded = num > len(blogs_data)
    return render_template('blog.html', posts=blogs_data, id=num, founded=not_founded)

if __name__ == '__main__':
    app.run(debug=True)