from tkinter import *

window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label
label = Label(text="Eau d'aromes", font=("Arial", 24, "bold"))
label.config(text="New Text")
label.grid(column=0, row=0,) 

#Advanced Python Argument


#Button 

def button_click():
    label.config(text=f"{input.get()}")

button = Button(text="Click Me", command=button_click)
button1 = Button(text="New button", command=button_click)
button1.grid(column=2, row=0)
button.grid(column=1, row=1)

#Entry

input = Entry(width=20)
input.grid(column=3, row=2)

#pack always in the middle of the program and you can change with side="left"
#place
#grid

window.mainloop()