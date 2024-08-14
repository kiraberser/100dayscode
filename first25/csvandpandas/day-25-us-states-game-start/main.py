import turtle
import pandas
from correct_state import State

#Crear la Pantalla
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#Crear el objeto estado
state = State()

#List de los estados que son correctos
guessed_state = []
wrong_list = []

#Llamar a la libreria pandas para leer csv y leer los estados de estados unidos
data = pandas.read_csv("50_states.csv")
states = data["state"]

while len(guessed_state) < 50:
    #Pregunta
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct", 
                                    prompt="What's another state's name?").title()
    #Si la respuesta es la misma
    if answer_state == "Exit":
        break
    correct_answer = data[states == answer_state] 
    if not correct_answer.empty:
        #Sacar las cordenadas del estado
        x_value = correct_answer['x'].values[0]
        y_value = correct_answer['y'].values[0]
        #Ocupar el objeto state y llamar al metodo correct_state en donde le pasamos valores
        state.correct_state(answer_state.capitalize(), x_value, y_value)
        guessed_state.append(answer_state)
    else:
        wrong_list.append(answer_state)
        df = pandas.DataFrame(wrong_list)
        df.to_csv("Wrong_States.csv")

    