from tkinter import *

#Screen
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

#First label
equal = Label(text="is equal to")
equal.grid(column=0, row=1)

#Input
entry = Entry(width=10)
entry.grid(column=1, row=0)

#Second label
miles = Label(text="Miles")
miles.grid(column=2, row=0)
km = Label(text="Km")
km.grid(column=2, row=1)

#Thirty label 
answer = Label(text="0")
answer.grid(column=1, row=1)

#convert miles to km
def milestokm():
    mile = entry.get()
    km = float(1.609 * mile)
    answer.config(text=f"{km}")

#button    
button = Button(text="Calculate", command=milestokm)
button.grid(column=1, row=2)


window.mainloop()
