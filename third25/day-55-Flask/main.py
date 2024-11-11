from flask import Flask
app = Flask(__name__)

def make_bold(route):
    def wrapper():
        return f'<strong>{route()}</strong>'
    return wrapper

def make_emphasis(route):
    def wrapper():
        return f'<em>{route()}</em>'
    return wrapper

def make_underlined(route):
    def wrapper():
        return f'<u>{route()}</u>'
    return wrapper

@app.route('/')
def home_page():
    return 'Home'

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return 'bye'


@app.route('/<name>/<int:number>')
def username(name, number):
    return f'Hello {name}!, your random number is {number}.'



if __name__ == "__main__":
    app.run(debug=True)