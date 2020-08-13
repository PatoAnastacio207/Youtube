import tkinter
import youtube_search

queue = []

def prueba(arg):
	print(arg)

def get_text_box():
	txt = text_box.get()
	text_box.insert(0, "")
	return txt

def add_song_to_queue(song):
	queue.append(song)
	update_queue()

def play_song(song):
	youtube_search.play_song(get_text_box())
	queue.pop()
	update_queue()

def update_queue():
	queue_str = ""
	for i in queue:
		queue_str += i + "\n"
	label["text"] = queue_str
	label.pack(ipady=10)

ventana = tkinter.Tk()
ventana.geometry("420x420")

text_box = tkinter.Entry(ventana)
text_box.pack(ipady=10)


boton1 = tkinter.Button(ventana, text="Buscar")
boton1.pack(ipady=10)

boton2 = tkinter.Button(ventana, text="generate label", command= lambda: add_song_to_queue(get_text_box()))
boton2.pack(ipady=10)

label = tkinter.Label(ventana)
label.pack(ipady=10)

ventana.mainloop()