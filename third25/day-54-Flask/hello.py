import time
from flask import Flask 
app = Flask(__name__)#execute only if run as script 

#Python decorators
@app.route('/')
def hello_world():
    return '<p>Hello World!</p>'

#Python decorators
@app.route('/blog')
def home_section():
    return '<p>Blog</p>\n' + '<a href="/">Back</a>'

if __name__ == "__main__":
    app.run()


#FUNCTIONS
#Functions can have inputs/functionality/output
#Functions are first-class objects, can be passed around as arguments e.g int/string/float
#Functions can be nested in other functions 
#Function can be returned from other functions 

#Python Decorator Function

#def delay_decorators(function):
#    def wrapper_function():
#        time.sleep(2)
#        function()
#    wrapper_function()
#    
#@delay_decorators
#def say_hello():
#    return "Hello"
#
#@delay_decorators
#def say_bye():
#    return "Bye"
#
#def say_greeting():
#   print("How are you?")
#print(say_bye)

