from flask import Flask, render_template, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from flask_bootstrap import Bootstrap5

from LoginForm import LoggingForm

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SECRET_KEY'] = 'oijdpasfdoijpodij2'
csrf = CSRFProtect(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    logForm = LoggingForm()
    if logForm.validate_on_submit():
        if 'admin@email.com' == logForm.email.data and '12345678' == logForm.password.data:
            return redirect(url_for('success'))
        else:
            return redirect(url_for('denied'))
    return render_template('login.html', form=logForm)

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/denied')
def denied():
    return render_template('denied.html')

if __name__ == '__main__':
    app.run(debug=True)
