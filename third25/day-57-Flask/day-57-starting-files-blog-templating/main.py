from flask import Flask, render_template

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
    all_post.get_post(id)
    return render_template('post.html', title=all_post.title, subtitle=all_post.subtitle, body=all_post.body)

if __name__ == "__main__":
    app.run(debug=True)
