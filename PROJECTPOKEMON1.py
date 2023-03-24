from PIL import ImageTk, Image
from tkinter import *

root = Tk()
root.geometry("600x400")
root.configure(bg="olive drab")
root.title("Pokemon Game")

# abra = ImageTk.PhotoImage(Image.open ( "abra.jpg"))
# bulbasour = ImageTk.PhotoImage(Image.open ( "bulbasour.jpg"))
# buttonP1 = ImageTk.PhotoImage(Image.open ( "button.jpg"))
# buttonP2 = ImageTk.PhotoImage(Image.open ( "button.jpg"))
# charmender = ImageTk.PhotoImage(Image.open ( "charmender.jpg"))
# lyvasour = ImageTk.PhotoImage(Image.open ( "lyvasour.jpg"))
# jigglypuff = ImageTk.PhotoImage(Image.open ( "jigglypuff.jpg"))
# kadabra = ImageTk.PhotoImage(Image.open ( "kadabra.jpg"))
# meowth = ImageTk.PhotoImage(Image.open ( "meowth.jpg"))
# nidoking = ImageTk.PhotoImage(Image.open ( "nidoking.jpg"))
# paras = ImageTk.PhotoImage(Image.open ( "paras.jpg"))
# persion = ImageTk.PhotoImage(Image.open ( "persion.jpg"))
# pikachu = ImageTk.PhotoImage(Image.open ( "pikachu.jpg"))
# ratata = ImageTk.PhotoImage(Image.open ( "ratata.jpg"))
# squirtle = ImageTk.PhotoImage(Image.open ( "squirtle.jpg"))

lblTitle = Label(root, text="Pokemon Game", bg="olive drab", fg="snow", font=("Curlz MT", 19, "bold", "italic")).place(relx=0.5,rely=0.075,anchor=CENTER)

lblPlayer1 = Label(root, text="Player 1", bg="dark olive green", fg="snow").place(relx=0.2,rely=0.2,anchor=CENTER)

lblPlayer2 = Label(root, text="Player 2", bg="dark olive green", fg="snow").place(relx=0.8,rely=0.2,anchor=CENTER)

lblScoreP1 = Label(root, bg="olive drab").place(relx=0.2,rely=0.4,anchor=CENTER)

lblScoreP2 = Label(root, bg="olive drab").place(relx=0.8,rely=0.4,anchor=CENTER)

lblRoll = Label(root, bg="olive drab").place(relx=0.5,rely=0.6,anchor=CENTER)

root.mainloop()