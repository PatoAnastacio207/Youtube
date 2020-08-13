import tkinter

window = tkinter.Tk()
window.geometry("400x300")

def delete():
    print(delete)
    entry.insert(0, "")

entry = tkinter.Entry(window)
entry.pack()

boton = tkinter.Button(window, command = delete)
boton.pack()


window.mainloop()