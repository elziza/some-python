# tkinter permet de creer des interfaces graphiques
from tkinter import *
from tkinter.ttk import *

# La strftime() méthode renvoie une chaîne représentant la date et
# l'heure à l'aide de l'objet date , time ou datetime .
from time import strftime

root = Tk()
root.title = ('clock')


def time():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000, time)


label = Label(root, font=("ds-digital", 80),
              background="black", foreground="cyan")

label.pack(anchor='center')
time()

root.mainloop()
