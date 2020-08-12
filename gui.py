import tkinter
import youtube_search

def prueba(arg):
	print(arg)

# youtube_search.start_window()

ventana = tkinter.Tk()
ventana.geometry("420x420")

text_box = tkinter.Entry(ventana)
text_box.pack()



def get_text_box():
	txt = text_box.get()
	text_box.insert(0, "")
	return txt

boton = tkinter.Button(ventana, text="Buscar", command= lambda: youtube_search.play_song(get_text_box()))
boton.pack()

ventana.mainloop()