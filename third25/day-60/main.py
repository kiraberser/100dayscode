from flask import Flask, render_template, request
from send_message import Send_Message

app = Flask(__name__)
gmail_message = Send_Message()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/contact', methods=['POST', 'GET'])
def receive_data():
    if request.method == 'POST':
        name = request.form['fN']
        email = request.form['email']
        number = request.form['phone-number']
        message = request.form['message']
        if name and email and number and message:
            gmail_message.send_email(email=email, name=name)
            return render_template('index.html', message=f'Succesfuly message {name.capitalize()}')
    return render_template('contact.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return f"<h1>Bienvenido {username}, Contraseña: {password}</h1> \n <a href='/form'>Volver a Log in</a>"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)