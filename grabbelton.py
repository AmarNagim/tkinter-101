from tkinter import *
import random
import time

window = Tk()
window.geometry("300x300")
items = ['laptop', 'deur', 'stoel', 'tafel', 'muis', 'telefoon', 'slipper', 'auto', 'fiets', 'lamp']

def text(label):
    l1=Label(window, text=label, font=("Arial", 10), anchor='center')
    l1.place(relx=0.5, rely=0.1, anchor=CENTER)
    return l1
        


def amount():
    amountElements = len(items)
    return amountElements
amountElements = amount()

def randomIntFunction():
    amountList = amount()
    if amountList == 0:
        return 0
    randomInt = random.randint(0, amount()-1)
    return randomInt
   


text(f"De grabbelton bevat {amount()} item(s)",)

def click():
    global items
    def back():
        amount = len(items)  
        text2 = text(f"           De grabbelton bevat {amount} item(s)               ")
    randomIntFunction()  
    if randomIntFunction != 0:  
        chosenItem = items[randomIntFunction()]
    else:
        chosenItem = 0   
               
    items.remove(chosenItem)
    text3 = text(f"Gefeliciteerd, je hebt {chosenItem} gegrabbelt!")
    Btn=Button(window, text="terug", anchor='center', command=back)
    Btn.place(relx=0.32, rely=0.2, anchor=CENTER)
    
    
    
Btn=Button(window, text="grabbelen", anchor='center', command=click)

        
Btn.place(relx=0.5, rely=0.2, anchor=CENTER)




window.mainloop()
