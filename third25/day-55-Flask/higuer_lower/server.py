#Llamamos dependencias
import random
from flask import Flask
#creamos el objeto
app = Flask(__name__)

#creamos un numero random entre 0 y 9
number = random.randint(0, 9)

#creamos un decorador donde verifica la logica del juego
def random_number_decorator(function):
    #args argunmentos posicionales 
    #kwargs argumenos con nombres 
    def wrapper(*args, **kwargs):
        guess = kwargs['guess']
        if guess < number:
            return('<h1>Too low, try again!</h1>' 
            '<img src="https://media.giphy.com/media/nR4L10XlJcSeQ/giphy.gif?cid=790b76113r14awsb0h2pflkgewigkq9nieeert9a6704kilg&ep=v1_gifs_search&rid=giphy.gif&ct=g"/>')
        elif guess > number:
            return('<h1>Too high, try again!</h1>' 
                    '<img src="https://media.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif?cid=790b76113r14awsb0h2pflkgewigkq9nieeert9a6704kilg&ep=v1_gifs_search&rid=giphy.gif&ct=g"/>')
        else:
            return('<h1>Congrats you win!</h1>' 
                '<img src="https://media.giphy.com/media/C9x8gX02SnMIoAClXa/giphy.gif?cid=790b76113r14awsb0h2pflkgewigkq9nieeert9a6704kilg&ep=v1_gifs_search&rid=giphy.gif&ct=g" />')          
    return wrapper

#ruta del juego y pasamos parametro
@app.route('/<int:guess>')
@random_number_decorator
def route_random_number(guess):
    return f'<h1>Your guess number is {guess}</h1>'
    
#ruta de la pagina principal
@app.route('/')
def home_page():
    return '<h1>Guess a number betewen 0 and 9</h1>' \
        '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"/>'

#Actualiza el codigo en cada cambio 
if __name__ == '__main__':
    app.run(debug=True)