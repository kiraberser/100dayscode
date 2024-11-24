from flask import Flask, render_template
app = Flask(__name__)

def name_decorator(function):
    def wrapper(*args, **kwargs):
        pass
    return wrapper()

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/blog')
def blog_page():
    return render_template('blog.html')

@app.route('/cv')
def cv_page():
    return render_template('cv.html')

if __name__ == "__main__":
    app.run(debug=True)

