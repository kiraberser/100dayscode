from flask import Flask, render_template, request, url_for, redirect, flash, session
from flask_wtf.csrf import CSRFProtect

from post import Post
from send_message import Send_Message
from LoginForm import LoggingForm

app = Flask(__name__)
csrf = CSRFProtect(app)

app.secret_key = 'oijdpasfdoijpodij2'

posts = Post()
send = Send_Message()

#Ruta home
@app.route('/')
def home():
    if 'user_is_logged_in' in session and session['user_is_logged_in']:
        username = session.get('username', 'Usuario') 
        is_logged = session.get('user_is_logged_in', 'Sesión iniciada')
        return render_template('index.html', username=username, posts=posts.data_blog, user_is_logged_in=is_logged)
    else:
        return render_template('index.html', posts=posts.data_blog)


#Ruta post
@app.route('/post/<int:id>')
def post(id):
    if 0 < id <= len(posts.data_blog):
        posts.get_post(id)
        return render_template('post.html', title=posts.title, subtitle=posts.subtitle, body=posts.body, image_url=posts.image)
    return render_template('error.html')

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        #Get all the data
        name = request.form['first-name']
        email= request.form['email']
        tel = request.form['phone-number']
        message = request.form['message']
        if name and email:
            #Send email message
            send.send_email(email=email, name=name, cel=tel, message=message)
            return redirect(url_for('contact', message_sended='Succesfuly sent your message'))
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['POST', 'GET'])
def receive_data():
    form = LoggingForm()
    try:
        if request.method == 'POST':
            username = form.username.data
            password = form.password.data
            if username == 'edwin' and password == '123456':
                session['user_is_logged_in'] = True
                session['username'] = username
                flash('Inicio de sesión exitoso', 'success')
                return redirect(url_for('home'))
            else:
                session['error'] = 'Nombre de usuario equivocado'
                return render_template('login.html', error=session['error'], form=form)
    except Exception as e:
        flash('Ocurrió un error inesperado. Inténtalo más tarde.', 'error')
        print('Error:', e)
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    session['user_is_logged_in'] = False
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
