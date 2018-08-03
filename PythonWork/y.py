import tkinter as tk


window = tk.Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('350x200')

lbl = tk.Label(window, text="Hello")

lbl.grid(column=0, row=0)

txt = tk.Entry(window,width=10)

txt.grid(column=1, row=0)

def clicked():

    res = "Welcome to " + txt.get()

    lbl.configure(text= res)

btn = tk.Button(window, text="Click Me", command=clicked)

btn.grid(column=2, row=0)
 
window.mainloop()
