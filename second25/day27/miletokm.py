from tkinter import *

#Screen

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=100)
window.config(padx=20, pady=20)

equal = Label(text="is equal to")
equal.grid(column=0, row=1)

entry = Entry(width=10)
entry.grid(column=1, row=0)

miles = Label(text="Miles")
miles.grid(column=2, row=0)
km = Label(text="Km")
km.grid(column=2, row=1)

answer = Label(text="")
answer.grid(column=1, row=1)

def milestokm():
    mile = int(entry.get())
    km = float(1.61 * mile)
    answer.config(text=f"{km}")
    
button = Button(text="Calculate", command=milestokm)
button.grid(column=1, row=2)


window.mainloop()
