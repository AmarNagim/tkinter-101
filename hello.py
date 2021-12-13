import tkinter as tk
from tkinter import font

window = tk.Tk()
window.title('Hello')
window.geometry('250x200')
window.configure(bg='lightblue')




box1 = tk.Label(
    window,
    text=("Hello\ntkinter!"),
    anchor="w",
    bg="blue",
    fg="white",
    
)
box1.config(font=("", 30))

box1.pack(
    expand=True,
    ipadx=5,
    ipady=5
)



window.mainloop()