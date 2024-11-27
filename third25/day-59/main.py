from flask import Flask, render_template, request

from post import Post
from send_message import Send_Message

app = Flask(__name__)
posts = Post()
send = Send_Message()

#Ruta home
@app.route('/')
def home():
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
        name = request.form['first-name']
        email= request.form['email']
        tel = request.form['phone-number']
        message = request.form['message']
        if name and email:
            send.send_email(email=email, name=name, cel=tel, message=message)
            return render_template('contact.html', message_sended='Succesfuly sent your message')
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['POST', 'GET'])
def receive_data():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username and password:
            return render_template('index.html', user=username, posts=posts.data_blog)
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)
