from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")    
    word_data = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

#data
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(word_data)
    canvas.itemconfig(word_text, text=f"{current_card["French"]}", fill="Black")
    canvas.itemconfig(title_text, text="French", fill="Black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, flip_card)
    
def flip_card():
    canvas.itemconfig(word_text, text=f"{current_card["English"]}", fill="White")
    canvas.itemconfig(title_text, text="English", fill="White")
    canvas.itemconfig(card_background, image=card_back)

def is_known():
    word_data.remove(current_card)
    data = pandas.DataFrame(word_data)
    data.to_csv("data/words_to_learn", index=False)
    next_card()
    
#screen
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

#canvas
canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

#images
card_background = canvas.create_image(400, 263, image=card_front)
title_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

#buttons
right = PhotoImage(file="images/right.png")
button_yes = Button(image=right, highlightthickness=0, command=is_known)
button_yes.grid(column=1, row=1)

wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong, highlightthickness=0, command=next_card)
button_wrong.grid(column=0, row=1)

#call the function when run the program 
next_card()

window.mainloop()




