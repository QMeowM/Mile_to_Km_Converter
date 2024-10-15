"""fix the layout tomorrow"""

from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=600, height=300)
window.config(padx=70, pady=60, background="White")

"""label"""

miles = Label(text="Miles", font=("Arial", 40, "normal"), foreground="black", background="white")
miles.grid(row=0,column=2)

km = Label(text="Km", font=("Arial", 40, "normal"), foreground="black", background="white")
km.grid(row=1,column=2)

is_equal_to = Label(text="is equal to", font=("Arial", 40, "normal"), foreground="black", background="white")
is_equal_to.grid(row=1,column=0)

n_km = Label(text="", font=("Arial", 40, "normal"), foreground="black", background="white")
n_km.grid(row=1,column=1)

"""Entry"""
n_miles = Entry(width=18, background="white", foreground="black", font=("Arial", 40, "normal"))
n_miles.insert(END, string="Enter number")
n_miles.focus()
n_miles.grid(row=0, column=1)

"""button"""
def convert():
    mi = n_miles.get()
    n_km.config(text=round(float(mi)*1.609344, 2))
button = Button(text="Calculate",font=("Arial", 40, "normal"), command=convert, background="white")
button.grid(row=2, column=1)

window.mainloop()