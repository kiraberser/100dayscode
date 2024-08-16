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
location_state = State()

#List de los estados que son correctos
guessed_state = []

#Llamar a la libreria pandas para leer csv y leer los estados de estados unidos
data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()

while len(guessed_state) < 50:
    #Pregunta
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct", 
                                    prompt="What's another state's name?").title()
    #Si la respuesta es la misma
    if answer_state == "Exit":
        missing_states = [state for state in states if state not in guessed_state]
        df = pandas.DataFrame(missing_states)
        df.to_csv("Missing_States.csv")
        break
    if answer_state in states and answer_state not in guessed_state:
        guessed_state.append(answer_state)
        state_data = data[data.state == answer_state]
        x = int(state_data.x)
        y = int(state_data.y)
        location_state.correct_state(answer_state, x, y)    
