from flask import Flask, render_template, request

#Peticiones
from post import Post

app = Flask(__name__)
all_post = Post()

#Ruta home
@app.route('/')
def home():
    return render_template('index.html', posts=all_post.data_blog)

#Ruta post
@app.route('/post/<int:id>')
def post(id):
    if 0 < id <= len(all_post.data_blog):
        all_post.get_post(id)
        return render_template('post.html', title=all_post.title, subtitle=all_post.subtitle, body=all_post.body, image_url=all_post.image)
    return render_template('error.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form')
def form():
    return render_template('login.html')

@app.route('/login', methods=['POST', 'GET'])
def receive_data():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username and password:
            return render_template('index.html', user=username, posts=all_post.data_blog)
    return render_template('login.html', user=username, posts=all_post.data_blog)

if __name__ == "__main__":
    app.run(debug=True)
