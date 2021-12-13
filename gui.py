import tkinter
import time

window = tkinter.Tk()

window.title('My First Window')
window.geometry('50x50')
print('Background 1')

def background2():
    window.configure(bg='pink')
    window.geometry('100x100')
    print('Background 2')
    
 
def background3():
    window.configure(bg='orange')
    window.geometry('150x150')    
    print('Background 3')

def background4():
    window.configure(bg='blue')
    window.geometry('200x200')     
    print('Background 4')

def background5():
    window.configure(bg='red')
    window.geometry('250x250')
    print('Background 5')

def background6():
    window.configure(bg='purple')
    window.geometry('300x300')    
    print('Background 6')

def destroy():
    window.destroy()
    print('BOOM!')

    
window.after(2000, background2)
window.after(4000, background3)
window.after(6000, background4)
window.after(8000, background5)
window.after(10000, background6)
window.after(12000, lambda:destroy())





window.mainloop()